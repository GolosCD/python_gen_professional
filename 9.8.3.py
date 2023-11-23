'''
Реализуйте декоратор trace, который выводит отладочную информацию о декорируемой функции во время ее выполнения, 
а именно: имя функции, переданные аргументы и возвращаемое значение в следующем формате:

TRACE: вызов <имя функции>() с аргументами: <кортеж позиционных аргументов>, <словарь именованных аргументов>
TRACE: возвращаемое значение <имя функции>(): <возвращаемое значение>
Также декоратор должен сохранять имя и строку документации декорируемой функции.

Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, 
а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор trace, но не код, вызывающий его.
'''

import functools

def trace(func: callable) ->callable:
    
    @functools.wraps(func)
    def wrapper(*args: tuple[str],**kwargs: dict[str:str]) ->callable:
       
        """ Декоратор выводит отладочную информацию о декорируемой функции"""
        
        print(f'TRACE: вызов {func.__name__}() с аргументами: {(*args,)}, {kwargs}')
        
        print(f"TRACE: возвращаемое значение {func.__name__}(): {repr(func(*args,**kwargs))}")
        
        return func(*args,**kwargs)
        
    return wrapper
    


# INPUT DATA:

# TEST_1:
@trace
def say(name, line):
    return f'{name}: {line}'
    
say('Jane', 'Hello, World')

# TEST_2:
@trace
def sub(a, b, c):
    '''прекрасная функция'''
    return a - b + c
    
print(sub.__name__)
print(sub.__doc__)
sub(20, 5, c=10)

# TEST_3:
@trace
def beegeek():
    '''beegeek docs'''
    return 'beegeek'

print(beegeek())    
print(beegeek.__name__)
print(beegeek.__doc__)

# TEST_4:
@trace
def add(a, b, c):
    '''docs'''
    return a + b + c

print(add(1, 2, 3))    
print(add.__name__)
print(add.__doc__)

# TEST_5:
@trace
def add(a, b, c):
    '''docs'''
    return a + b + c

print(add(b=3, c=3, a=3))    
print(add.__name__)
print(add.__doc__)

# TEST_6:
@trace
def concat(a, b):
    '''concat two strings'''
    return a + b

print(concat('bee', b='geek'))    
print(concat.__name__)
print(concat.__doc__)

# TEST_7:
@trace
def func(nums):
    '''прекрасная функция'''
    return list(i**2 for i in nums)
    
print(func.__name__)
print(func.__doc__)
func([1, 2, 3, 4, 5, 6])

# TEST_8:
@trace
def func(nums, degree=3):
    '''прекрасная функция'''
    return list(i**degree for i in nums)

print(func.__name__)
print(func.__doc__)
func([1, 2, 3, 4, 5, 6], degree = 5)