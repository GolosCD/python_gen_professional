'''
Итератор RandomNumbers
Реализуйте класс RandomNumbers, порождающий итераторы, конструктор которого принимает три аргумента в следующем порядке:

left — целое число
right — целое число
n — натуральное число
Итератор класса RandomNumbers должен генерировать последовательность из n случайных чисел от left до right включительно, 
а затем возбуждать исключение StopIteration.

Примечание 1. Гарантируется, что left <= right.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый класс RandomNumbers.
'''
from random import randint

class RandomNumbers:

    def __init__(self,left,right,n):
        self.n = n
        self.num = randint(left,right)
        self.counter = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        self.counter+=1
        if self.counter-1<self.n:
            return self.num
        else:
            raise StopIteration
            
            
# INPUT DATA:

# TEST_1:
iterator = RandomNumbers(1, 1, 3)

print(next(iterator))
print(next(iterator))
print(next(iterator))

# TEST_2:
iterator = RandomNumbers(1, 10, 2)

print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))

# TEST_3:
iterator = RandomNumbers(-100, -92, 99)

print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))
print(next(iterator) in range(-100, -91))

# TEST_4:
iterator = RandomNumbers(5, 5, 98)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

# TEST_5:
iterator = RandomNumbers(1000, 1001, 108)

print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))
print(next(iterator) in range(1000, 1002))

# TEST_6:
iterator = RandomNumbers(-100, 99, 100)

print(next(iterator) in range(-100, 100))
print(next(iterator) in range(-100, 100))
print(next(iterator) in range(-100, 100))
print(next(iterator) in range(-100, 100))
print(next(iterator) in range(-100, 100))
print(next(iterator) in range(-100, 100))
print(next(iterator) in range(-100, 100))

# TEST_7:
iterator = RandomNumbers(-1000, -900, 1)

print(next(iterator) in range(-1000, -899))

try:
    next(iterator)
except StopIteration:
    print('Error')

# TEST_8:
iterator = RandomNumbers(-1000, -900, 4)

print(next(iterator) in range(-1000, -899))
print(next(iterator) in range(-1000, -899))
print(next(iterator) in range(-1000, -899))
print(next(iterator) in range(-1000, -899))

try:
    next(iterator)
except StopIteration:
    print('Error')