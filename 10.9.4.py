'''
Функция take()
Реализуйте функцию take(), которая принимает два аргумента в следующем порядке:

iterable — итерируемый объект
n — натуральное число
Функция должна возвращать итератор, генерирующий последовательность из первых n элементов итерируемого объекта iterable.

Примечание 1. Элементы итерируемого объекта в возвращаемом функцией итераторе должны располагаться в своем исходном порядке.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию take(), но не код, вызывающий ее.
'''
import itertools as it

def take(iterable,n):
    yield from it.compress(iterable,[True]*n)
    
    
    
    
    
# INPUT DATA:

# TEST_1:
print(*take(range(10), 5))

# TEST_2:
iterator = iter('beegeek')

print(*take(iterator, 22))

# TEST_3:
iterator = iter('beegeek')

print(*take(iterator, 1))

# TEST_4:
iterator = take(iter('beegeek'), 2)

print(next(iterator))
print(next(iterator))

# TEST_5:
iterator = iter('stepik')

print(*take(iterator, 6))

# TEST_6:
iterator = iter('stepik')

print(*take(iterator, 5))

# TEST_7:
iterator = iter('s')

print(*take(iterator, 1))

# TEST_8:
iterator = iter([0])

print(*take(iterator, 100))

# TEST_9:
print(list(take([], 100)))    
