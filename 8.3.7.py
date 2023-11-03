'''
Реализуйте функцию recursive_sum() с использованием рекурсии, которая принимает два аргумента в следующем порядке:

a — неотрицательное целое число
b — неотрицательное целое число
Функция должна возвращать сумму чисел a и b. При вычислении суммы функция:

не должна использовать циклы
из всех арифметических операций должна использовать только +1 и −1
Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию recursive_sum(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print(recursive_sum(10, 22))
Sample Output 1:

32
Sample Input 2:

print(recursive_sum(99, 0))
Sample Output 2:

99
Sample Input 3:

print(recursive_sum(0, 0))
Sample Output 3:

0
'''

def recursive_sum(a:int, b:int)->int:
    if a==0:
        return b
    else: 
        return recursive_sum(a-1, b+1)
        
        
print(recursive_sum(10, 22))