'''
Функция take_nth()
Реализуйте функцию take_nth(), которая принимает два аргумента в следующем порядке:

iterable — итерируемый объект
n — натуральное число
Функция должна возвращать n-ый по счету элемент итерируемого объекта iterable. Если итерируемый объект iterable содержит менее n элементов, функция должна вернуть значение None.

Примечание 1. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию take_nth(), но не код, вызывающий ее.
'''
import itertools as it

def take_nth(iterable,n):
    result =  it.islice(iterable,n-1,n)    
    return next(result,None)


# INPUT DATA:

# TEST_1:
numbers = [11, 22, 33, 44, 55]

print(take_nth(numbers, 3))

# TEST_2:
iterator = iter('beegeek')

print(take_nth(iterator, 4))

# TEST_3:
iterator = iter('beegeek')

print(take_nth(iterator, 10))

# TEST_4:
iterator = iter('beegeek')

print(take_nth(iterator, 1))

# TEST_5:
iterator = tuple('stepik')

print(take_nth(iterator, 6))

# TEST_6:
iterator = iter('p')

print(take_nth(iterator, 1))

# TEST_7:
iterator = iter('p')

print(take_nth(iterator, 2))

# TEST_8:
iterator = iter('beegeek')

print(take_nth(iterator, 7))

# TEST_9:
iterator = iter('beegeek')

print(take_nth(iterator, 8))

# TEST_10:
print(take_nth([], 4))
