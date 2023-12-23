'''
Функция is_rising()
Реализуйте функцию is_rising(), которая принимает один аргумент:

iterable — итерируемый объект, элементами которого являются числа
Функция должна возвращать True, если элементы итерируемого объекта расположены строго по возрастанию, или False в противном случае.

Примечание 1. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством, а также содержит не менее двух элементов.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_rising(), но не код, вызывающий ее.
'''

#Первое решение
from itertools import tee,zip_longest

def is_rising(iterable):
    
    iter_general,iter_second = tee(iterable)
    
    next(iter_second,None)
    
    return all(
               map(
                   lambda x: x[0]<x[1], 
                   zip_longest(iter_general,iter_second,fillvalue = 300)
                   )
              )
#Второе решение
from itertools import pairwise,starmap


is_rising = lambda iterable: all(starmap(lambda x,y: x<y,pairwise(iterable)))
    
    
    
    
    
# INPUT DATA:

# TEST_1:
print(is_rising([1, 2, 3, 4, 5]))

# TEST_2:
iterator = iter([1, 1, 1, 2, 3, 4])

print(is_rising(iterator))

# TEST_3:
iterator = iter(list(range(100, 200)))

print(is_rising(iterator))

# TEST_4:
iterator = iter(list(range(200, 100, -1)))

print(is_rising(iterator))

# TEST_5:
iterator = iter(list(range(100, 201)) + [200])

print(is_rising(iterator))

# TEST_6:
iterator = iter([10]*50)

print(is_rising(iterator))    
