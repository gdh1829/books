#!/usr/bin/python3

def isList(data):
    return (list == type(data))

def isNone(data):
    return (None == data)

def isEmpty(data):
    return (0 == len(data))

def hasOnlyNumber(data):
    for ele in data:
        if int != type(ele):
            return False
    return True