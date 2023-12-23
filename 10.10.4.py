'''
Функция ncycles()
Реализуйте функцию ncycles(), которая принимает два аргумента в следующем порядке:

iterable — итерируемый объект
times — натуральное число
Функция должна возвращать итератор, генерирующий последовательность элементов итерируемого объекта iterable, зацикленных times раз.

Примечание 1. Элементы итерируемого объекта в возвращаемом функцией итераторе должны располагаться в своем исходном порядке.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию ncycles(), но не код, вызывающий ее.
'''

import itertools as it

ncycles = lambda iterable,times: it.chain.from_iterable(it.tee(iterable,times))

# def ncycles(iterable,times):
    # yield from it.chain.from_iterable(it.tee(iterable,times))


# INPUT DATA:

# TEST_1:
print(*ncycles([1, 2, 3, 4], 3))

# TEST_2:
iterator = iter('bee')

print(*ncycles(iterator, 4))

# TEST_3:
iterator = iter([1])

print(*ncycles(iterator, 10))

# TEST_4:
iterator = ncycles(iter('b'), 1)

print(next(iterator))

# TEST_5:
iterator = ncycles(iter('g'), 3)

print(next(iterator))
print(next(iterator))
print(next(iterator))

# TEST_6:
iterator = ncycles(iter([10, 10, 10, 10, 10]), 5)

print(*iterator)

# TEST_7:
print(list(ncycles([], 5)))