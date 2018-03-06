def moveDisc(howMany, startPeg, tempPeg, endPeg):
    if howMany == 1:
        print("Move from " + str(startPeg) + " to " + str(endPeg))
    else:
        moveDisc(howMany - 1, startPeg, endPeg, tempPeg)
        moveDisc(1, startPeg, tempPeg, endPeg)
        moveDisc(howMany - 1, tempPeg, startPeg, endPeg)
moveDisc(4, 1, 2, 3)
