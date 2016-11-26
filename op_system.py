# coding=utf-8

import os

print dir(os)


os.mkdir('mydir')
os.chdir('mydir')
print os.getcwd()
open('file1.txt', 'w')
open('file2.txt', 'w')
print os.listdir('.')

os.remove('file1.txt')
os.unlink('file2.txt')

import os.path
print os.path.isfile('file1.txt')
print os.path.isdir('file1.txt')


print os.path.join('a','b','c')             # preferred way for cross-platforms solutions

os.chdir('..')
os.rmdir('mydir')

for path, dirs, files in os.walk('/usr/lib/gcc'):
    print path, dirs, files

print "-"*20

for path, dirs, files in os.walk('/usr/lib/gcc'):
    if 'cc1' in files:
        print path


import shutil                               # some additional FS functions

import tempfile                             # for temp files exist during program execution

f = tempfile.TemporaryFile()                # file exists in memory. it has no name and is available only for our program PID
print f

f = tempfile.NamedTemporaryFile()           # for creating real file in /tmp . For example for exchange between PIDs
print f.name

raw_input("?")

f.close
