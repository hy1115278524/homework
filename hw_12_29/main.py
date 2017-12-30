#!/usr/bin/env python
# encoding: utf-8
# Author: Feniox

import os
import time

def handle(num1, num2):
    '''handle function
       would handle two number.
    '''
    result = [num1, num2, num1+num2]
    return result[::-1]

with open('/root/workspace/pack/log'+time.strftime("%Y%m%d")+'.txt', 'a+') as f:
    print("please enter two number:")
    num1 = int(input("first number:"))
    num2 = int(input("second number:"))
    result = handle(num1, num2)
    f.write(str(result)+'\n')

source = ['/root/workspace/pack']

target = '/root/workspace/hw'

if not os.path.exists(target):
    os.mkdir(target)


today = target + os.sep + time.strftime("%Y%m%d")

now = time.strftime('%H%M%S')

comment = input("Enter a comment:")

if len(comment)==0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
        comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory!', today)

zip_command = 'zip -r {0}{1}'.format(target, ' '.join(source))

print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAULED')
