#!/usr/bin/python3

# Python 3.6.8

# fact func는 모든 음이 아닌 정수에 대해 다음과 같이 재귀 방식으로 정의할 수 있다.
# fact(n) = n * fact(n-1), if n > 1
#         = 1, if n = 1
# int n을 인수로 받아 n의 계승을 반환하는 함수를, 재귀를 사용하는 방식과 사용하지 않는 방식 두 가지로 작성하기

import time
from decorators import timer

userInput = int(input("Input any number: "))
EXCEPTION_NON_POSITIVE_NUMBER = 'num argument has to be positive number.'

# Non-Recursive way
def factWithoutRecursive(num):
    if 0 >= num:
        raise Exception(EXCEPTION_NON_POSITIVE_NUMBER)
    
    if 1 == num:
        return num

    result = num
    for i in range(num-1, 0, -1):
        result *= i
    
    return result

# Recursive way
def factWithRecursive(num):
    if 0 >= num:
        raise Exception(EXCEPTION_NON_POSITIVE_NUMBER)
    
    if 1 == num:
        return num
    
    return num * factWithRecursive(num-1)

@timer
def runA(num):
    factWithoutRecursive(num)

@timer
def runB(num):
    factWithRecursive(num)

runA(userInput)
runB(userInput)

print(factWithoutRecursive(userInput))
print(factWithRecursive(userInput))

