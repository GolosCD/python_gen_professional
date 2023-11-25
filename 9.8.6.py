'''
Реализуйте декоратор repeat, который принимает один аргумент:

times — натуральное число
Декоратор должен вызывать декорируемую функцию times раз.

Также декоратор должен сохранять имя и строку документации декорируемой функции.

Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, 
а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор repeat, но не код, вызывающий его.
'''

import functools


import functools


def repeat (time :int) -> callable:
    def decorator(func :callable) ->callable:
        """Декоратор повтора выполнения принимаем функций"""
        
        @functools.wraps(func)
        def wrapper(*args :list[str],**kwargs :dict[str:str]) ->callable:
            
            # result = func(*args,**kwargs)
            
            for _ in range(time+1):
                
                result = func(*args,**kwargs)
            return result
                    
            
        return wrapper
    return decorator
    
    
# INPUT DATA:

# TEST_1:
@repeat(3)
def say_beegeek():
    '''documentation'''
    print('beegeek')
    
say_beegeek()
"""
# TEST_2:
@repeat(4)
def say_beegeek():
    '''documentation'''
    print('beegeek')
    
print(say_beegeek.__name__)
print(say_beegeek.__doc__)

# TEST_3:
@repeat(1)
def beegeek():
    '''beegeek docs'''
    print('beegeek')
    
print(beegeek.__name__)
print(beegeek.__doc__)
beegeek()

# TEST_4:
@repeat(10)
def beegeek():
    '''beegeek docs'''
    print('beegeek')
    
print(beegeek.__name__)
print(beegeek.__doc__)
beegeek()
"""
# TEST_5:
@repeat(10)
def add(a, b):
    '''sum of two numbers'''
    return a + b
    
print(add.__name__)
print(add.__doc__)
print(add(10, b=20))
"""
# TEST_6:
counter = 0

@repeat(11)
def change_counter():
    global counter
    counter += 1
    print(counter)
    
print(change_counter.__name__)
print(change_counter.__doc__)
change_counter()
print(counter)

# TEST_7:
@repeat(5)
def say(word):
    print(word)

say(word="Hey!")    """