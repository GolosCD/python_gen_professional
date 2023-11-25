'''
Реализуйте декоратор add_attrs, который принимает произвольное количество именованных аргументов и 
устанавливает их в качестве атрибутов декорируемой функции. Названием атрибута должно являться имя аргумента, 
значением атрибута — значение аргумента.

Также декоратор должен сохранять имя и строку документации декорируемой функции.

Примечание 1. Вспомните про атрибут функции __dict__.

Примечание 2. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, 
а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимый декоратор add_attrs, но не код, вызывающий его.
'''
import functools

def add_attrs (**attrs :dict[str:str|int]) ->callable:
    def decorator (func :callable) ->callable:
        for key in attrs:
            setattr(func,key,attrs.get(key))

        # или можно было так func.__dict__ |= attrs просто добавляем словарь к словарю.

        @functools.wraps(func)
        def wrapper(*args :tuple[str],**kwargs :dict[str:str|int]) ->callable:
            """Декоратор добавляет заданные атриубты к функции"""
            
            return func(*args,**kwargs)

        return wrapper
    return decorator


# INPUT DATA:

# TEST_1:
@add_attrs(attr1='bee', attr2='geek')
def beegeek():
    return 'beegeek'

print(beegeek.attr1)
print(beegeek.attr2)

# TEST_1:
# bee
# geek

# TEST_2:
@add_attrs(attr2='geek')
@add_attrs(attr1='bee')
def beegeek():
    return 'beegeek'
    
print(beegeek.attr1)
print(beegeek.attr2)
print(beegeek.__name__)

# TEST_2:
# bee
# geek
# beegeek

# TEST_3:
@add_attrs(attr1='bee', attr2='geek', attr3='stepik')
def beegeek():
    return 'beegeek'
    
print(beegeek.attr1)
print(beegeek.attr2)
print(beegeek.attr3)
print(beegeek.__name__)
print(beegeek.__doc__)

# TEST_3:
# bee
# geek
# stepik
# beegeek
# None

# TEST_4:
@add_attrs(at1=10, at2=20, at3=30, at4=40, atf=50)
def add(a, b):
    '''add docs'''
    return a + b
    
print(add.at1)
print(add.at2)
print(add.at3)
print(add.__name__)
print(add.__doc__)
print(add(1, 2))
print(add(b=12, a=13))
print(add.at4)
print(add.atf)

# TEST_4:
# 10
# 20
# 30
# add
# add docs
# 3
# 25
# 40
# 50

# TEST_5:
@add_attrs(func_attr='i am attribute')
def func(a, b):
    '''func docs'''
    return
    
print(func.func_attr)

# TEST_5:
# i am attribute