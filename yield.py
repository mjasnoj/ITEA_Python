# coding utf-8

# async/await

def f(x, y):
    if x:
        return 2 * y

f(x,g(a, b, c))


# значние г не будет вычисляться сразу же, а будет вычислено только если x > 0
# g() можно задать как генератор и откладывать вычисления. Генератор не будет сразу же вычисляться


"""
>>> def inf_list():
...     i = 0
...     while true:
...             yield i
...             i += 1



>>> def inf_list():
...     i=0
...     while True:
...             yield i
...             i+=1
...
>>> for i in inf_list():
...     if i * i > 100:
...             break
...     print i
...
0
1
2
3
4
5
6
7
8
9
10

"""

"""
>>> import itertools
>>> list(itertools.takewhile(lambda i: i*i <= 100, itertools.count()))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> list(itertools.permutations('ABC',2))
[('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

>>> [x*x for x in range(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> (x*x for x in range(10))
<generator object <genexpr> at 0x7f93572a7aa0>
>>> g=(x*x for x in range(10))
>>> g.next()
0
>>> g.next()
1
>>> g.next()
4

"""
