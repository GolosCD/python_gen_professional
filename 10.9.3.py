'''
Функция first_true()
Реализуйте функцию first_true(), которая принимает два аргумента в следующем порядке:

iterable — итерируемый объект
predicate — функция-предикат; если имеет значение None, то работает аналогично функции bool()
Функция first_true() должна возвращать первый по счету элемент итерируемого объекта iterable, для которого функция predicate вернула значение True. Если такого элемента нет, функция first_true() должна вернуть значение None.

Примечание 1. Предикат — это функция, которая возвращает True или False в зависимости от переданного в качестве аргумента значения.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию first_true(), но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

numbers = [1, 1, 1, 1, 2, 4, 5, 6]

print(first_true(numbers, lambda num: num % 2 == 0))
Sample Output 1:

2
Sample Input 2:

numbers = iter([1, 1, 1, 1, 2, 4, 5, 6, 10, 100, 200])

print(first_true(numbers, lambda num: num > 10))
Sample Output 2:

100
Sample Input 3:

numbers = (0, 0, 0, 69, 1, 1, 1, 2, 4, 5, 6, 10, 100, 200)

print(first_true(numbers, None))
Sample Output 3:

69
'''


from itertools import compress

def first_true(iterable , predicate = None):
    if not predicate: predicate = bool;
    iterable = list(iterable)    
    
    return_val = compress(iter(iterable),map(predicate, iterable))

    try: 
        a = list(return_val)[0] 
    
    except: 
        a = None
    return a    

        
        
# INPUT DATA:

# TEST_1:
numbers = [1, 1, 1, 1, 2, 4, 5, 6]

print(first_true(numbers, lambda num: num % 2 == 0))

# TEST_2:
numbers = iter([1, 1, 1, 1, 2, 4, 5, 6, 10, 100, 200])

print(first_true(numbers, lambda num: num > 10))

# TEST_3:
numbers = (0, 0, 0, 69, 1, 1, 1, 2, 4, 5, 6, 10, 100, 200)

print(first_true(numbers, None))

# TEST_4:
numbers = (0, 0, 0, 69, 1, 1, 1, 2, 4, 5, 6, 0, 10, 100, 200)
numbers_iter = filter(None, numbers)

print(first_true(numbers_iter, lambda num: num < 0))

# TEST_5:
numbers = [10000]

print(first_true(numbers, lambda num: num % 2 == 0))

# TEST_6:
numbers = [10000]

print(first_true(numbers, lambda num: num % 2 == 1))

# TEST_7:
numbers = iter([1, 1, 1, 1, 2, 4, 5, 6, 10, 100, 200])

print(first_true(numbers, lambda num: num == 200))

# TEST_8:
numbers = iter([])

print(first_true(numbers, lambda num: num == 200))