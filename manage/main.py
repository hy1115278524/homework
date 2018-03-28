#!/usr/bin/env python
# encoding: utf-8
# Author: Feniox

import json
from  datetime import datetime, timedelta
import os
import logging

logging.basicConfig(level=logging.INFO,
                    filename='./log/log.txt',
                    filemode='w',
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

class Model(object):
    '''
    对用户信息进行保存，删除或新增用户文件
    '''
    User = []
    def save(self):
        filename = './User/' + self.name + '.txt'
        with open(filename, 'w+') as f:
            data = json.dumps(self.__dict__)
            f.write(data)

    def delete(self):
        file = './User/' + self.name + '.txt'
        if os.path.exists(file):
            os.remove(file)

    def find(self, name):
        if name in self.__class__.user:
            filename = './User/' + name + '.txt'
            with open(filename) as f:
                s = f.read()
                data = json.loads(s)
            return data

class Bill(Model):
    '''
    创建一个新的账单或查看所有账单
    '''
    def new_bill(self, type_info, money):
        t = datetime.now()
        delta = timedelta(hours=8)
        T = t - delta
        now = T.strftime('%Y%m%d_%H%M%S')
        self.accounts[type_info] = (money, now)
        self.save()
        logging.info(self.name+' '+type_info+' '+str(money)+'￥ Successful!')

    def find_bill(self):
        data = self.find(self.name)
        all_accounts = data['accounts']
        return all_accounts

class Borrow(Bill):
    '''
    用户可以借钱还钱
    '''
    interest = 0.02

    def borrow(self, money):
        if money>self.available and self.credit < 10:
            return 'borrow error!'

        else:
            self.available -= money
            self.balance += money
            logging.info(self.name+' want to borrow '+str(money)+'￥')
            self.new_bill('borrow', money)
            return 'borrow successful!'

    def repay(self, money):
        self.available += money*(1 - self.__class__.interest)
        self.balance -= money
        self.credit += 1
        logging.info(self.name+' want to repay '+str(money)+'￥')
        self.new_bill('repay', money)



class Count(Bill):
    '''
    用户可以查看自己的消费情况.
    '''
    def reporting(self, time):
        all_accounts = self.find_bill()
        report_list = []
        report_str = ''
        for k, v in all_accounts.items():
            if v[1][0:8] == time:
                report_list.append((k, v))
        for typeinfo, info in report_list:
            report_str += 'Type:{0}  you expend {1}￥ on {2}\n'.format(typeinfo, info[0], info[1])
        return report_str

class Balance(Bill):
    '''
    用户可以存钱和取钱
    '''
    def deposit(self, money):
        self.balance += money
        logging.info(self.name+' want to deposit '+str(money)+'￥')
        self.new_bill('deposit', money)

    def draw(self, money):
        if self.balance >= money:
            self.balance -= money
            logging.info(self.name+' want to draw '+str(money)+'￥')
            self.new_bill('draw', money)
        else:
            return 'balance is not enough!'

class User(Borrow, Count, Balance):
    '''
    用户类
    '''
    user = []
    def __init__(self, name, sex, ID):
        self.name = name
        self.sex = sex
        self.ID = ID
        self.balance = 0
        self.credit = 15
        self.available = 2000
        self.accounts = {}
        self.__class__.user.append(self.name)

harden = User('harden', 'man', '111')
harden.deposit(200)
harden.draw(50)
harden.borrow(300)
harden.repay(30)
rep = harden.reporting('20180328')
print(rep)



