'''
Реализуйте декоратор takes, который принимает произвольное количество позиционных аргументов, каждый из которых является типом данных.

Декоратор должен проверять, что аргументы, передаваемые в декорируемую функцию, принадлежат одному из этих типов. 
Если хотя бы один аргумент не принадлежит одному из данных типов, декоратор должен возбуждать исключение TypeError.

Также декоратор должен сохранять имя и строку документации декорируемой функции.

Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, 
а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
'''
import functools,typing

def takes (*take_args,**take_kwargs) -> callable:
    def decorator(func :callable) ->callable:
        """Декоратор замены символов в заданном диапазоне внутри стринга"""
        
        @functools.wraps(func)
        def wrapper(*args,**kwargs) ->callable:
            
            types :set = set((*take_args,*take_kwargs))
            
            func_args :set = set((type(i) for i in [*args,*kwargs.values()]))

            if func_args.issubset(types):
                return func(*args,**kwargs)
                
            raise TypeError    
           
        return wrapper
    return decorator




# import functools,typing

# def takes (*take_args,**take_kwargs) -> callable:
    # def decorator(func :callable) ->callable:
        # """Декоратор замены символов в заданном диапазоне внутри стринга"""
        
        # @functools.wraps(func)
        # def wrapper(*args,**kwargs) ->callable:
            
            # types :list = tuple((*take_args,*take_kwargs))
            
            # print(types)
            # print()
            # print([*args,*kwargs])
            
            # result: bool = all(map(lambda x: True if isinstance(x,types) else False,[*args,*kwargs]))
            
            # if result:
                # return func(*args,**kwargs)
            
            # raise TypeError
            
        # return wrapper
    # return decorator
    

# TEST_11:
@takes(str)
def beegeek(word, repeat):
    return word * repeat
    
try:
    print(beegeek('beegeek', repeat=2))
except TypeError as e:
    print(type(e)) 


# INPUT DATA:

# TEST_1:
@takes(int, str)
def repeat_string(string, times):
    return string * times

print(repeat_string('bee', 3))
"""
# TEST_2:
@takes(list, bool, float, int)
def repeat_string(string, times):
    return string * times

try:
    print(repeat_string('bee', 4))
except TypeError as e:
    print(type(e))

# TEST_3:
@takes(list)
def append_this(li, elem):
    '''append_this docs'''
    return li + [elem]

print(append_this.__name__)
print(append_this.__doc__)

try:
    print(append_this([1, 2], [3, 4]))
except TypeError as e:
    print(type(e))

# TEST_4:
@takes(list)
def append_this(li, elem):
    '''append_this docs'''
    return li + [elem]

print(append_this.__name__)
print(append_this.__doc__)

try:
    print(append_this([1, 2], 3))
except TypeError as e:
    print(type(e))
"""
# TEST_5:
@takes(str, int, list)
def add(a, b):
    '''add docs'''
    return a + b

print(add.__name__)
print(add.__doc__)

try:
    print(add('a', 'b'))
except TypeError as e:
    print(type(e))
"""
# TEST_6:
@takes(list, int, tuple, str)
def add(a, b):
    '''add docs'''
    return a + b

print(add.__name__)
print(add.__doc__)

try:
    print(add(a='a', b='c'))
except TypeError as e:
    print(type(e))

# TEST_7:
@takes(list, int, tuple, str)
def add(a, b):
    '''add docs'''
    return a + b

print(add.__name__)
print(add.__doc__)

try:
    print(add(1, b=2))
except TypeError as e:
    print(type(e))

# TEST_8:
@takes(list, int, float, str)
def add(a, b):
    '''add docs'''
    return a + b

print(add.__name__)
print(add.__doc__)

try:
    print(add((1, 2), (3, 4, 5)))
except TypeError as e:
    print(type(e))

# TEST_9:
@takes()
def beegeek():
    '''beegeek docs'''
    return 'beegeek'
    
print(beegeek())

# TEST_10:
@takes(str)
def beegeek(word):
    return word

print(beegeek(word="beegeek"))

"""
   