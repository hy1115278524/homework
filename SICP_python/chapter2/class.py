#!/usr/bin/env python
# encoding: utf-8
# Author: Feniox
import math

class Account(object):
    '''A bank account that has a non-negative balance.'''
    poundage = 0.08

    def withdraw(self, money):
        '''Decrease the account balance by amount and return the new balance.'''
        if money>self.balance:
            print("Insufficient funds")
        self.balance -= (1 + Account.poundage)*money
        return self.balance

    def save(self, money):
        '''Increase the account balance by amount and return the new balance.'''
        self.balance += money
        return self.balance

    def showaccount(self):
        print("balance is {0}".format(self.balance))

class BorrowAccount(Account):
    interest = 0.08
    def cborrow(self, money, time):
        '''Increase the account balance by borrowing money.'''
        self.borrow = math.pow(1+self.__class__.interest, time) * money
        self.available_borrow -= self.borrow
        self.balance += self.borrow
        return self.available_borrow

class RepayAccount(Account):
    def repay(self, money):
        '''Decrease the account balance by repay money.'''
        if money>self.borrow:
            print("repay error")
        else:
            self.borrow -= money
            self.balance -= money

class Caccount(BorrowAccount, RepayAccount):
    '''Create a new account.'''
    def __init__(self):
        self.balance = 1
        self.available_borrow = 8000
        self.borrow = 0



Jim_account = Caccount()
Jim_account.save(20)
Jim_account.cborrow(30, 2)
Jim_account.repay(20)
Jim_account.showaccount()
