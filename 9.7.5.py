'''
Реализуйте декоратор takes_positive, который проверяет, 
что все аргументы, передаваемые в декорируемую функцию, являются положительными целыми числами.

Если хотя бы один аргумент не удовлетворяет данному условию, декоратор должен возбуждать исключение:

TypeError, если аргумент не является целым числом
ValueError, если аргумент является целым числом, но отрицательным или равным нулю
Примечание 1. Приоритет возбуждения исключений при несоответствии аргумента обоим 
условиям или при наличии разных аргументов, несоответствующих разным условиям: TypeError, затем ValueError.

Примечание 2. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, 
а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимый декоратор takes_positive, но не код, вызывающий его.
'''
from typing import Any

def takes_positive(func: callable) ->callable:
    '''Декоратор - проверки значений передаваемой функции'''

    def inner(*args: tuple[Any],**kwargs: dict[str:Any]) ->Any:
        
        #кидаю в сет, что бы не проверять дубли, а они есть
        total_set: set = set([*args,*kwargs.values()])

        if not all(map(lambda x: isinstance(x,int),total_set)):
            raise TypeError
        
        #вторая проверка всех значений не нужна. просто проверьте минимальное число
        elif min(total_set)<0:
            raise ValueError
        
        else:
            return func(*args,**kwargs)
                     
    return inner

# INPUT DATA:

# TEST_1:
@takes_positive
def positive_sum(*args):
    return sum(args)
    
print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# TEST_2:
@takes_positive
def positive_sum(*args):
    return sum(args)
    
try:
    print(positive_sum(-3, -2, -1, 0, 1, 2, 3))
except Exception as err:
    print(type(err))

# TEST_3:
@takes_positive
def positive_sum(*args):
    return sum(args)
    
try:
    print(positive_sum('10', 20, 10))
except Exception as err:
    print(type(err))

# TEST_4:
@takes_positive
def positive_sum(*args):
    return sum(args)
    
try:
    print(positive_sum(10, 20, 16, 18, '10'))
except Exception as err:
    print(type(err))

# TEST_5:
@takes_positive
def positive_sum(*args):
    return sum(args)
    
try:
    print(positive_sum(10, 20, '16', 18, '10'))
except Exception as err:
    print(type(err))

# TEST_6:
@takes_positive
def positive_sum(*args):
    return sum(args)
    
print(positive_sum(*range(10, 100)))

# TEST_7:
@takes_positive
def positive_sum(*args):
    return sum(args)
    
try:
    print(positive_sum(3, 2, 1, -8, 1, 2, 3))
except Exception as err:
    print(type(err))

# TEST_8:
@takes_positive
def positive_sum(*args):
    return sum(args)
    
try:
    print(positive_sum(*range(100, -1, -1)))
except Exception as err:
    print(type(err))

# TEST_9:
@takes_positive
def positive_sum(*args, **kwargs):
    return sum(args) + sum(kwargs.values())
    
print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, par1=1, sep=4))

# TEST_10:
@takes_positive
def positive_sum(*args, **kwargs):
    return sum(args) + sum(kwargs.values())
    
try:
    print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, par1=1, sep=-40))
except Exception as err:
    print(type(err))

# TEST_11:
@takes_positive
def positive_sum(*args, **kwargs):
    return sum(args) + sum(kwargs.values())
    
try:
    print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, par1=1, sep='40'))
except Exception as err:
    print(type(err))

# TEST_12:
@takes_positive
def positive_sum(*args):
    return sum(args)
    
try:
    print(positive_sum(11, 20.7, 10))
except Exception as err:
    print(type(err))

# TEST_13:
@takes_positive
def power(a, n):
    return a**n
    
try:
    print(power(a="3", n="2"))
except Exception as err:
    print(type(err))