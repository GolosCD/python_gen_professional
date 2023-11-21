'''
Реализуйте декоратор reverse_args, который передает все позиционные аргументы в декорируемую функцию func в обратном порядке.

Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также должен 
уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор reverse_args, но не код, вызывающий его.﻿
'''

def reverse_args(func: callable)-> callable:
    '''Декоратор для функции, разворачивает массив с аргументами функции в обратный порядок'''
    
    def decor_engine(*args:tuple[int],**kwargs: dict [str,int])-> callable:
        return func(*args[::-1],**kwargs)
    return decor_engine
    
    
# INPUT DATA:

# TEST_1:
@reverse_args
def power(a, n):
    return a ** n
    
print(power(2, 3))

# TEST_2:
@reverse_args
def concat(a, b, c):
    return a + b + c
    
print(concat('apple', 'cherry', 'melon'))

# TEST_3:
@reverse_args
def operation(a, b, c):
    return a // b + c
    
print(operation(10, 20, 80))

# TEST_4:
@reverse_args
def operation(a, b):
    return a // b
    
print(operation(90, 0))

# TEST_5:
@reverse_args
def operation(a, b):
    return a // b

try:
    print(operation(0, 70))
except ZeroDivisionError:
    print('ZeroDivisionError')

# TEST_6:
@reverse_args
def operation(a, b, name):
    return a // b + name
    
print(operation(10, 90, name=1))

# TEST_7:
@reverse_args
def operation(a, b, value=10):
    return a // b + value

try:
    print(operation(0, 70))
except ZeroDivisionError:
    print('ZeroDivisionError')

# TEST_8:
@reverse_args
def operation(a, b, value=10):
    return a // b - value

print(operation(70, 70, value=70))


# OUTPUT DATA:

# TEST_1:
9

# TEST_2:
meloncherryapple

# TEST_3:
14

# TEST_4:
0

# TEST_5:
ZeroDivisionError

# TEST_6:
10

# TEST_7:
ZeroDivisionError

# TEST_8:
-69