#!/usr/bin/env python
# encoding: utf-8
# Author: Feniox

#This esercise just want to tell you how to use "global"
#and "nonlocal"

import datetime

variable_x = 10
variable_y = 20

def Modify():
    '''Modify() function can modify
       global variable.
    '''
    global variable_x
    variable_x = 15
    print("now x={0}".format(variable_x))
    return None

def LocalModify():
    '''LocalModify() function can modify
       local variable.
    '''
    variable_z = 15
    def Change():
        nonlocal variable_z
        variable_z = 18
        Observe()
        return None
    def Observe():
        print("now z = {0}".format(variable_z))
        return None
    return Change

if __name__ == "__main__":
    now = datetime.datetime.now()
    Modify()
    end = datetime.datetime.now()
    LocalModify()()
    Time = end - now
    print("Total running time:{0:.6}s".format(Time.total_seconds()))
