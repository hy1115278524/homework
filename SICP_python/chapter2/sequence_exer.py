#!/usr/bin/env python
# encoding: utf-8
# Author: Feniox

#我们需要解决的问题是将100以内的奇数的平方进行相加

def hander(k):
    if(k%2!=0):
        return k

def square(k):
    return k*k

L = tuple(map(square, filter(hander, range(1,101))))
S = sum(L)
print(S)

#我们利用生成器表达式来求解
L2 = tuple(x*x for x in range(1,100) if x%2!=0)
S2 = sum(L2)
print(S2)


