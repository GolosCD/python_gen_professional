'''
Реализуйте декоратор prefix, который принимает два аргумента в следующем порядке:

string — произвольная строка
to_the_end — булево значение, по умолчанию равное False
Декоратор должен добавлять строку string к возвращаемому значению декорируемой функции. 
Если to_the_end имеет значение True, строка string добавляется в конец, если False — в начало.

Также декоратор должен сохранять имя и строку документации декорируемой функции.

Примечание 1. Гарантируется, что возвращаемым значением декорируемой функции является объект типа str.

Примечание 2. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, 
а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимый декоратор prefix, но не код, вызывающий его.
'''
import functools

def prefix(string :str,to_the_end :bool=False) ->callable:
    def decorator(func) ->callable:
        @functools.wraps(func)
        def wrapper(*args,**kwargs):

            total_list = list(func(*args,**kwargs))
            if to_the_end:
                total_list+=[string]
            else:
                total_list=[string]+total_list
            print()
            return ''.join(total_list)
            
        return wrapper
    return decorator        



# INPUT DATA:

# TEST_1:
@prefix('€')
def get_bonus():
    return '2000'
    
print(get_bonus())

# TEST_2:
@prefix('$$$', to_the_end=True)
def get_bonus():
    return '2000'
       
print(get_bonus())

# TEST_3:
@prefix(' online-school', to_the_end=True)
def beegeek():
    '''beegeek docs'''
    return 'beegeek'
       

print(beegeek.__name__)
print(beegeek.__doc__)
print(beegeek())

# TEST_4:
@prefix('online-school ')
def beegeek():
    '''beegeek docs'''
    return 'beegeek'
       

print(beegeek.__name__)
print(beegeek.__doc__)
print(beegeek())

# TEST_5:
@prefix('online-school ')
def make_lower(string, lower=True):
    '''makes string upper or lower'''
    if lower:
        return string.lower()
    return string.upper()
       

print(make_lower.__name__)
print(make_lower.__doc__)
print(make_lower('beegeek', False))

# TEST_6:
@prefix(' rocks', True)
def make_lower(string, lower=True):
    '''makes string upper or lower'''
    if lower:
        return string.lower()
    return string.upper()
       

print(make_lower.__name__)
print(make_lower.__doc__)
print(make_lower('Beegeek'))

# TEST_7:
@prefix('online-school ')
def make_lower(string, lower=True):
    if lower:
        return string.lower()
    return string.upper()


print(make_lower('beegeek', lower=False))