import math
def insertShiftArray(array, number): # will take an array nad a number to insert it

        index = len(array) / 2
        if index % 2 ==0 :
            array.insert(int(index), number)
        elif index % 2 != 0 :
            index = index - (index%2)
            index = math.ceil(index)
            index +=1
            array.insert(index, number)
