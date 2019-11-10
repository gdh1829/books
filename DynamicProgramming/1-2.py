#!/usr/bin/python3

# Python 3.6.8

# 정수 값의 배열이 주어졌을 때 배열의 각 원소를 누적합으로 갱신하는 재귀 함수를 작성해보자. 
# 예를 들어, 입력 배열이 다음과 같이 있다면 
# [1, 2, 3, 4, 5, 6]
# 이 함수는 위의 배열을 다음과 같이 갱신해야 한다.
# [1, 3, 6, 10, 15, 21]

# Native
import random
# Custom
import validator
from decorators import timer

arr = [random.randint(-10, 10) for i in range(10)]
EXCEPTION_NO_DATA = 'No data'
EXCEPTION_NOT_NUMBER_TYPE = 'Only number type is allowed'
EXCEPTION_NOT_LIST = 'List is required'

def before(arr):
    if validator.isNone(arr) or validator.isEmpty(arr):
        raise Exception(EXCEPTION_NO_DATA)
    
    if not validator.isList(arr):
        raise Exception(EXCEPTION_NOT_LIST)

    if not validator.hasOnlyNumber(arr):
        raise Exception(EXCEPTION_NOT_NUMBER_TYPE)


# Non recursive way
def testWithNonRecursive(arr):
    
    before(arr)
    
    if 1 == len(arr):
        return arr
    
    result = []
    for index in range(len(arr)):
        result.append(sum(result, arr, index))
    
    return result

def sum(base, arr, index):
    return arr[index] if 0 == len(base) else base[len(base) - 1] + arr[index]



# recursive way
def testWithRecursive(arr):
    before(arr)

    if 1 == len(arr):
        return arr
    result = [arr[0]]
    return fibonacci(result, arr, 1)

def fibonacci(base, arr, index):
    if index == len(arr):
        return base

    base += [base[index-1] + arr[index]]
    
    return fibonacci(base, arr, index + 1)
    
@timer
def runA(data):
    testWithNonRecursive(data)

@timer
def runB(data):
    testWithRecursive(data)

runA(arr)
runB(arr)


print('Original: ' + arr.__str__())
print('Non Recursive Way Result: ' + testWithNonRecursive(arr).__str__())
print('Recursive Way Result: ' + testWithRecursive(arr).__str__())