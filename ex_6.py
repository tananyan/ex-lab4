#!/usr/bin/env python3
import json
# import sys
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gens import field, gen_random
from librip.iterators import Unique as unique

path = 'data_light.json'
'''try:
    path = sys.argv[1]
except IndexError:
    raise ValueError('Path to data file is not specified')'''
# Здесь необходимо в переменную path получить
# путь до файла, который был передан при запуске

# with open(path) as f:
# data = json.load(f)
with open('data_light.json', 'r', encoding='utf-8') as fh:  # открываем файл на чтение
    data = json.load(fh)  # загружаем из файла данные в словарь data


# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Важно!
# Функции с 1 по 3 дожны быть реализованы в одну строку
# В реализации функции 4 может быть до 3 строк
# При этом строки должны быть не длиннее 80 символов

@print_result
def f1(arg):
    l1 = list(unique(field(arg, 'job-name'), ignore_case=True))
    sorted(l1, key=lambda x: x.lower())
    return l1


@print_result
def f2(arg):
    return list(filter(lambda x: x if x.find('Программист') == 0 else '', arg))
    # list(filter(lambda x: x.lower().startswith('программист'), arg))

    # raise NotImplemented


@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))
    # raise NotImplemented


@print_result
def f4(arg):
    # zp = gen_random(100000,200000,len(arg))
    zp = [' c зарплатой ' + str(x) for x in gen_random(100000, 200000, len(arg))]
    return list(map(lambda x: x[0] + '' + x[1], zip(arg, zp)))

with timer():
    f4(f3(f2(f1(data))))

'''def search():
    for x in l1:
        x = x.lower()

        if x.find('программист') == 0:
            return x'''

# print(', '.join(map(str, unique(field(data, 'job-name')))))
# l1 = list(unique(field(data, 'job-name'), ignore_case=True))
# sorted(l1, key=lambda x: x.lower())
# l2 = list(filter(lambda x: x if x.find('Программист') == 0 else '', l1))

# print((f1(data)))
# print(f2(data))
# print((f1(data)))

# p = f1(data)

'''def sum_all(*args):
    s = 0
    for el in args:
        s = el
    return s'''

# print(sum_all('f','d','d','a'))
# s = 'rtgyrKHBh'


# print(l1[6].startswith('gg'))

# print(l1[4])
'''l = ['c erg' + str(345345) for i in range(5)]
print(l)
# rand = gen_random(100000,200000,len(l))
zp = [' c зарплатой ' + str(x) for x in gen_random(100000, 200000, 5)]
print(list(zp))'''


x = ['fd', 'd', 'sd']
y = ['1','2','3']
print(list(zip(x,y)))
