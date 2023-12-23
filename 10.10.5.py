'''
Функция grouper()
Реализуйте функцию grouper(), которая принимает два аргумента в следующем порядке:

iterable — итерируемый объект
n — натуральное число
Функция должна возвращать итератор, генерирующий последовательность, элементами которой являются объединенные в кортежи по n элементов соседние элементы итерируемого объекта iterable. 
Если у элемента не достаточно соседей, то ими становится значение None.

Примечание 1. Элементы итерируемого объекта в возвращаемом функцией итераторе должны располагаться в своем исходном порядке.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию grouper(), но не код, вызывающий ее.
'''


import itertools as it  

grouper =  lambda iterable,n: it.zip_longest(*it.repeat(iter(iterable),n))

    
    
    
# INPUT DATA:

# TEST_1:
numbers = [1, 2, 3, 4, 5, 6]

print(*grouper(numbers, 2))

# TEST_2:
iterator = iter([1, 2, 3, 4, 5, 6, 7])

print(*grouper(iterator, 3))

# TEST_3:
iterator = iter([1, 2, 3])

print(*grouper(iterator, 5))

# TEST_4:
iterator = iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(*grouper(iterator, 4))

# TEST_5:
iterator = iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(*grouper(iterator, 5))

# TEST_6:
iterator = iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(*grouper(iterator, 1))

# TEST_7:
iterator = iter('beegeek')

print(*grouper(iterator, 5))

# TEST_8:
iterator = iter('beegeek')

print(*grouper(iterator, 20))
