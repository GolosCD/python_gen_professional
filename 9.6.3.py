'''
Реализуйте функцию cyclic_shift() с использованием аннотаций типов, которая принимает два аргумента в следующем порядке:

numbers — список целых или вещественных чисел
step — целое число
Функция должна изменять переданный список, циклически сдвигая элементы списка на step шагов, и возвращать значение None. 
Если step является положительным числом, сдвиг происходит вправо, если отрицательным — влево.

Примечание 1. Используйте встроенные типы (list, tuple, ...), а не типы из модуля typing. Также используйте нотацию |, а не тип Union из модуля typing.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию cyclic_shift(), но не код, вызывающий ее. 
'''
from collections import deque 

def cyclic_shift(numbers: list[int|float], step: int)->None:
    tmp_deque:list = deque(numbers)
    tmp_deque.rotate(step)
    numbers[:] = tmp_deque        





# # TEST_1:
numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, 1)

print(numbers)
# # TEST_1:
# [5, 1, 2, 3, 4]

# TEST_2:
numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, -2)

print(numbers)
# # TEST_2:
# [3, 4, 5, 1, 2]

# TEST_3:
numbers = [1, 2.0, 3, 4.0, 5.5]
cyclic_shift(numbers, 0)

print(numbers)

# TEST_4:
annotations = cyclic_shift.__annotations__

print(annotations['return'])
print(annotations['step'])

# TEST_5:
print(*cyclic_shift.__annotations__.values())

# TEST_6:
numbers = [234, 33, 4, 6, 2, 4, 75, 34, 1, 3, 6, 3, 3]
cyclic_shift(numbers, 7)

print(numbers)

# TEST_7:
numbers = [234, 33, 4, 6, 2, 4, 75, 34, 1, 3, 6, 3, 3, 2, 54, 65, 7, 8, 9]
cyclic_shift(numbers, -11)

print(numbers)

# TEST_8:
numbers = [234]
cyclic_shift(numbers, 10)

print(numbers)

# TEST_9:
numbers = [234]
cyclic_shift(numbers, -20)

print(numbers)

# TEST_10:
numbers = [234, 235]
cyclic_shift(numbers, 15)

print(numbers)

# TEST_11:
numbers = [234, 235]
cyclic_shift(numbers, -22)

print(numbers)


# # OUTPUT DATA:

# # TEST_1:
# [5, 1, 2, 3, 4]

# # TEST_2:
# [3, 4, 5, 1, 2]

# # TEST_3:
# [1, 2.0, 3, 4.0, 5.5]

# # TEST_4:
# None
# <class 'int'>

# # TEST_5:
# list[int | float] <class 'int'> None

# # TEST_6:
# [75, 34, 1, 3, 6, 3, 3, 234, 33, 4, 6, 2, 4]

# # TEST_7:
# [3, 3, 2, 54, 65, 7, 8, 9, 234, 33, 4, 6, 2, 4, 75, 34, 1, 3, 6]

# # TEST_8:
# [234]

# # TEST_9:
# [234]

# # TEST_10:
# [235, 234]

# # TEST_11:
# [234, 235]