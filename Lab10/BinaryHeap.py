__author__ = 'guinnc'

class BinaryHeap:
    ''' The book's BinaryHeap class.
    '''

    def __init__(self):
        '''
        Create an empty heap.
        :return: Nothing.
        '''
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self,i):
        '''
        Percolate the value at index i up in the tree.
        :param i: The index of the value to move up in the tree.
        :return: Nothing.
        '''
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
               tmp = self.heapList[i // 2]
               self.heapList[i // 2] = self.heapList[i]
               self.heapList[i] = tmp
            i = i // 2

    def insert(self,k):
        '''
        Inserts a value into the binary heap.
        :param k: The value to insert into the tree.
        :return: Nothing.
        '''
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self,i):
        '''
        Percolate the value at index i down in the tree.
        :param i: The index of the value to percolate down.
        :return: Nothing.
        '''
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self,i):
        '''
        Find the index of the child of "i" which is smallest.
        :param i: The index of the parent node.
        :return: The index of the smallest child.
        '''
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        ''' Remove and return the minimum value of the heap.
        :return: The smallest value in the heap.
        '''
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self,alist):
        '''
        Create a binary heap from the values in the list, alist.
        :param alist: The values to insert into the heap.
        :return: Nothing.
        '''
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1

myHeap=BinaryHeap()
myHeap.insert(9)
myHeap.insert(5)
myHeap.insert(6)
myHeap.insert(2)
myHeap.insert(3)

smallest=myHeap.delMin()
print("Min is", smallest)


