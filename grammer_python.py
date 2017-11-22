#!/usr/bin/env python
# encoding: utf-8
# Author: Feniox

#in python stmt is combined by simple_stmt and compound_stmt
#so we can divide it in two parts to discuss


#in first parts we discuss simple_stmt,so what is simple_stmt mean?
#simple_stmt: small_stmt (';' small_stmt)* [';'] NEWLINE
#apparently,we know that simple_stmt contains one or more samll_stmt
#Then,small_stmt: (expr_stmt | del_stmt | pass_stmt | flow_stmt |
#import_stmt | global_stmt | nonlocal_stmt | assert_stmt)
#from that we clear know that how to form simple_stmt

#expr_stmt
a = 1
b = 2
a += 1
b -= 2
(c,d)=(2,3)
a += b

#del stmt
del a
del (c,d)

#pass_stmt
#pass

#flow_stmt
def f():
    for i in range(5):
        if(i==1):
            continue
        elif(i==2):
            yield 2
            pass
        elif(i==3):
            return i
        raise "error"


#global_stmt
#(a,b)=(1,2)
global q

#nonlocal_stmt
#nonlocal t

#assert_stmt
assert 1

#Next,we are able to discuss compound_stmt
#compound_stmt: if_stmt | while_stmt | for_stmt | try_stmt |
#with_stmt | funcdef | classdef | decorated | async_stmt

#if_stmt
if 1:
    def tt(f):
        pass
    def ttt(a):
        pass
    @tt
    @ttt
    def f():
        pass
    class A():
        pass

#while_stmt
a = 1
while a > 0:
    y = 2
    a -= 1
else:
    print("y={0}".format(y))




#for_stmti
for x in range(5):
    if 1:
        pass
    def tt(f):
        pass
else:
    print(2)



#try_stmt
try:
    pass
except:
    pass
else:
    pass
finally:
    pass



#with_stmt
with open("./t.py") as f:
    pass


#funcdef
def f(x:int,*args,**kwargs)->(int,int):
    def ff():
        pass
    class A():
        pass
    try:
        pass
    except:
        pass
    if 1:
        pass


#classdef
class A:
    def f():
        pass
    class B:
        pass

#decorated

def tt(f):
    pass
def ttt(a):
    pass
@tt
@ttt
class F:
    pass

#async_stmt
async def main():
    await tt

#lambda
lambda x: x**2

#up to now we can basically to combine python's grammer
