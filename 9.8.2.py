'''
Реализуйте декоратор returns_string, который проверяет, что возвращаемое значение декорируемой функции принадлежит типу str. 
Если возвращаемое значение принадлежит какому-либо другому типу, декоратор должен возбуждать исключение TypeError.

Также декоратор должен сохранять имя и строку документации декорируемой функции.

Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, 
а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор returns_string, но не код, вызывающий его.
'''

import functools

def returns_string(func: callable) ->callable:
    
    @functools.wraps(func)
    def wrapper(*args: tuple[str],**kwargs: dict[str:str]) ->callable:
        """ Декоратор проверять, что введеные значения это str"""
        
        if isinstance(func(*args,**kwargs),str):
            return func(*args,**kwargs)
        else:
            raise TypeError
            
    return wrapper
    


# INPUT DATA:

# TEST_1:
@returns_string
def beegeek():
    return 'beegeek'
    
print(beegeek())

# TEST_2:
@returns_string
def add(a, b):
    return a + b

try:
    print(add(3, 7))
except TypeError as e:
    print(type(e))

# TEST_3:
@returns_string
def beegeek():
    '''documentation'''
    return 'beegeek'

print(beegeek.__name__)
print(beegeek.__doc__)

# TEST_4:
@returns_string
def nothing():
    return

print(nothing.__name__)
print(nothing.__doc__)

try:
    nothing()
except TypeError as e:
    print(type(e))

# TEST_5:
@returns_string
def add(a, b):
    '''docs'''
    return a + b

print(add.__name__)
print(add.__doc__)

try:
    add([1, 2], [3, 4])
except TypeError as e:
    print(type(e))

# TEST_6:
@returns_string
def concat(a, b):
    '''concat two strings'''
    return a + b

print(concat.__name__)
print(concat.__doc__)
print(concat('10', b='20'))

# TEST_7:
@returns_string
def concat(*args, **kwargs):
    return "".join([*args, *kwargs.values()])

print(concat("Hello ", x="world", y="!!!"))