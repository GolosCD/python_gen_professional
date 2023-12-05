'''
Реализуйте генераторную функцию primes(), которая принимает два аргумента в следующем порядке:

left — натуральное число
right — натуральное число
Функция должна возвращать генератор, порождающий последовательность простых чисел от left до right включительно, 
а затем возбуждающий исключение StopIteration.

Примечание 1. Гарантируется, что left <= right.

Примечание 2. Простое число — натуральное число, имеющее ровно два различных натуральных делителя — единицу и самого себя. 
Единица простым числом не является. 

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую генераторную функцию primes(), но не код, вызывающий ее.
'''
from math import sqrt


def primes(left :int, right :int) ->int:

    is_prime = lambda n: all( n%i != 0 for i in range(2, int(sqrt(n))+1) )
    
    for i in range(max(2,left),right+1):
        if is_prime(i):
            yield i
            


# INPUT DATA:

# TEST_1:
generator = primes(1, 15)

print(*generator)

# TEST_2:
generator = primes(6, 36)

print(next(generator))
print(next(generator))

# TEST_3:
generator = primes(37, 37)

try:
    print(next(generator))
    print(next(generator))
except StopIteration:
    print('Error')

# TEST_4:
generator = primes(39, 83)

print(*generator)

# TEST_5:
generator = primes(43, 79)

print(*generator)

# TEST_6:
generator = primes(43, 72)

print(*generator)

# TEST_7:
generator = primes(1000, 2000)

print(*generator)

# TEST_8:
generator = primes(2000, 100000)

for _ in range(1000):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))  
       