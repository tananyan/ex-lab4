#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [4, 1, 2, 1, 1, 2, 1, 2, 3, 2]
data2 = gen_random(5, 10, 9)
data3 = ['a', 'A', 'b', 'B', 'c', 'c', 'C', 'f']

# Реализация задания 2

print('data:', data1)
print('unique:', ', '.join(map(str, Unique(data1))))
print()

print('data:', data2)
print('unique:', ', '.join(map(str, Unique(data2))))
print()

print('data:', data3, 'ignore_case:', True)
print('unique:', ', '.join(map(str, Unique(data3, ignore_case=True))))
print()

print('data:', data3, 'ignore_case:', False)
print('unique:', ', '.join(map(str, Unique(data3))))
print()

print(list(map(str, Unique(data3))))
