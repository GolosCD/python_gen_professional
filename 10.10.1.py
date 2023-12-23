'''
Функция sum_of_digits()
Реализуйте функцию sum_of_digits(), которая принимает один аргумент:

iterable — итерируемый объект, элементами которого являются натуральные числа
Функция должна возвращать единственное число — сумму цифр всех чисел, присутствующих в итерируемом объекте iterable.

Примечание 1. Рассмотрим набор чисел 13,20,41,2,2,5 из первого теста. 
Сумма цифр всех представленных чисел будет равна:1+3+2+0+4+1+2+2+5=20
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию sum_of_digits(), но не код, вызывающий ее.
'''
from itertools import chain

sum_of_digits = lambda x: sum(map(int,chain.from_iterable(map(str,x))))

    
# INPUT DATA:

# TEST_1:
print(sum_of_digits([13, 20, 41, 2, 2, 5]))

# TEST_2:
print(sum_of_digits((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))

# TEST_3:
print(sum_of_digits([123456789]))

# TEST_4:
numbers = [10]*100

iterator = iter(numbers)
print(sum_of_digits(iterator))

# TEST_5:
numbers = [100, 20, 30, 400, 500, 5]*100000

print(sum_of_digits(numbers))    
