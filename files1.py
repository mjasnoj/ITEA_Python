# coding=utf-8
f = open("file.txt", 'wt')

"""
w - write (open for write and delete if already exists)
r - read (open for read)
a - append (open for write and no rewrite - append to the end)
x -
t - text file (is needed to avoid problems with \n\r)

Python3 - строки в юникоде
"""

print f.tell()          # 0 byte of file

f.write("Some string1\n")
f.write("Some string2\n")
f.write("Some string3\n")

print f.tell()


"""
file write using FS buffer.
Only after file close or buffer overload data will be written to disk
"""

f.flush()

f.write("Some string1\n")
f.write("Some string2\n")
f.write("Some string3\n")

f.close()

"""
Когда завершается выполнения скрипта закрываются все файлы которые он использовал
Если одноразовый скрипт - можно файлы не закрывать
Если же приложение работает 24х7 то необходимо по окончанию работы с файлами закрывать файл


Файлы не блокируются при открытии. Несколько разных процессов могут писать в один и тот же файл
"""

"""
fcntl

LOCK_SH - shared lock (for read)
LOCK_EX - exclusive lock (for write)
LOCK_UN - unlock (for unlock)

not need for Windows
"""

f = open("file.txt", 'at')
print f.tell()

f.write("Some string1\n")
f.write("Some string2\n")
f.write("Some string3\n")

f.close()

print "------------------------------------"

f = open("file.txt", 'rt')
print f.tell()

s = f.read()
print f.tell()

print s

print f.read()

f.close()

print "------------------------------------"

f = open("file.txt", 'rt')
print f.readline()

f.close()

print "------------------------------------"


f = open("file.txt", 'rt')
print f.read(11)
print f.read(16)

f.close()

print "------------------------------------"
"""pythonway"""
f = open("file.txt", 'rt')
for line in f:
    print line

f.close()

print "------------------------------------"

f = open('file.txt', 'r+t')
"""
read and write
"""

f.read(10)
f.tell()
f.write("1123123")

f.seek(-5,2)
print f.tell()
f.write("FAFAFAFAFA")

f.seek(-5,2)
print f.tell()
f.write("B")

f.close()
