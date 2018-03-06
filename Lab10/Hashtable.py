__author__ = 'guinnc'
''' HashTable class from book listings 5_5, 5_6, 5_7, and 5_8.
    Note that I've written a slightly more complicated hashfunction method
    that allows for the key to be either a string or an integer. '''

import math

class HashTable:
    def __init__(self):
        '''
        Constructor sets the default number of slots to 11.
        '''
        self.length = 0
        self.size = 7001
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def makeTableBigger(self):
        '''
        Increase the table size to first prime larger than 2 times the current size.
        The Big-O of this method is O(n) because it has to hash and store all of the old values into the new table.
        :return: No return value.
        '''

        #first let's save the old keys and data
        oldSlots = list(self.slots)
        oldData = list(self.data)

        # double the table size and find the next prime after that
        newSize = 2 * self.size + 1 # add 1 to make it odd
        while not self.isPrime(newSize):
            newSize += 2 # adding 2 because I only want to check odd numbers

        self.size = newSize
        self.length = 0
        self.slots = [None] * self.size
        self.data = [None] * self.size

        # now we need to copy the old keys/data into the new table
        for index in range(len(oldSlots)):
            if oldSlots[index] != None:
                self.put(oldSlots[index], oldData[index])


    def put(self, key, data):
        ''' Inserts data into the hash table using the key.
        :param key: An integer or string used as the hash value.
        :param data: The data to be inserted.
        :return: Nothing is returned.
        '''

        if self.length/self.size >= 0.5:
            self.makeTableBigger()

        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None or self.slots[hashvalue] == "ReMoVeD_23457":
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
            self.length += 1
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  # replace
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and \
                                self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                    self.length += 1
                else:
                    self.data[nextslot] = data  # replace


    def hashfunction(self, key, size):
        '''
        Computes the index given a particular key.
        :param key: An integer or string used as the key.
        :param size: The size of the hash table.
        :return: The computed index.  This method may thrown an exception
        if the key is not an integer or a string.
        '''
        if type(key) is int:
            return key % size
        elif type(key) is str:
            sum = 0
            for pos in range(len(key)):
                sum = sum + ord(key[pos])

            return sum % size
        else:
            raise Exception("Invalid key in hash function: " + str(key))


    def rehash(self, oldhash, size):
        '''
        Returns a new hash value.  Used in the event of a collision.  Linear probing
        is the resolution.
        :param oldhash: The old hash value.
        :param size: The size of the hash table.
        :return: The new hash value.
        '''
        return (oldhash + 1) % size


    def get(self, key):
        '''
        Retrieves the data from the hash table at a particular key.
        :param key: The key to use to retrieve the data.
        :return: The data at a particular key.
        '''
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and \
                not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data


    def __getitem__(self, key):
        ''' Overrides getitem so that a programmer can use the square bracket notation.
        :param key: The key in the hash table.
        :return: The value at that key.
        '''
        return self.get(key)


    def __setitem__(self, key, data):
        ''' Overrides setitem so that a programmer can use the square bracket notation.
        :param key: The key to use.
        :param data: The data to store at that key.
        :return: Nothing returned.
        '''
        self.put(key, data)

    def __len__(self):
        '''
        Returns the number of elements that have been inserted into the hash table. The big-O is O(1).
        :return: The number of elements in the hash table.
        '''
        return self.length

    def delete(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and \
                not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
                # here's the laz remove
                self.slots[position] = "ReMoVeD_23457"
                self.length -= 1

            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def isPrime(self, number):
        '''
        Computes whether a number is prime or not.  Big-O is O(SQRT(n)).
        :param number: The number to check.
        :return: True if prime; false, otherwise.
        '''
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        sqrtNumber = math.sqrt(number)
        for divisor in range(3, int(sqrtNumber) + 1, 2):
            if number % divisor == 0:
                return False
        return True





