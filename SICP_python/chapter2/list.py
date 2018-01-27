#!/usr/bin/env python
# encoding: utf-8
# Author: Feniox


def make_list():
    contents = None
    first = None
    rest = None
    def dispatch(method, value=None):
        nonlocal contents
        nonlocal first
        nonlocal rest
        if method=="push":
            contents = (value, contents)
            first, rest = contents[0], contents[1]
            return contents
        elif method=="pop":
            temp = contents[0]
            if contents!=None:
                first, rest = contents[0], contents[1]
                contents = contents[1]
            else:
                first = rest = None
            return temp
        elif method=="getitem":
            temp1, temp2 = contents[0], contents[1]
            while(temp1!=None):
                if(temp2==None):
                    temp1 = None
                if(temp1==value):
                    return True
                temp1, temp2 = temp2[0], temp2[1]
            return False
    return dispatch


L = make_list()

L("push", 1)
L("push", 2)
L("push", 3)
L("push", 4)

t = L("pop")
print(t)
t2 = L("getitem", 2)
print(t2)




