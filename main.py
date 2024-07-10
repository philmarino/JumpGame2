import os
import sys

def jump(list):
    resultSet = jumpIterator(list, 0, 0)
    smallest = sys.maxsize
    smallestResult = []
    for each in resultSet:
        if len(each) < smallest:
            smallest = len(each)
            smallestResult = each
    print(smallest - 1)
    print(smallestResult)

def jumpIterator(list, startingPoint, depth):
    resultSet = []
    if startingPoint > len(list):
        return resultSet
    if startingPoint == len(list)-1:
        resultSet.append([startingPoint])
        return resultSet
    for index in range(1, list[startingPoint]+1):
        lower = jumpIterator(list, startingPoint+index, depth+1)
        for each in lower:
            additive = [startingPoint]
            additive.extend(each)
            resultSet.append(additive)

    return resultSet


#Example 1:
#Input: 
nums = [2,3,1,1,4]
ret = jump(nums)
#print(ret.narrative)
#Output: 2
#Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.


#Example 2:
#Input: 
nums = [2,3,0,1,4]
ret = jump(nums)
#if ret:
#Output: 2

 