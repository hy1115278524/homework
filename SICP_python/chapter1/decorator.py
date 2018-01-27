#!/usr/bin/env python
# encoding: utf-8
# Author: Feniox

def func(fn):
    def f(x, y):
        print("after operation,the result as follow:")
        result = fn(x, y)
        print(result)
        return None
    return f

@func
def add(x, y):
    return x + y

@func
def substraction(x, y):
    return x - y

@func
def mul(x, y):
    return x * y

add(1, 2)
substraction(3, 4)
mul(4, 5)
