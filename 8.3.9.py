'''
Последовательность Трибоначчи – последовательность натуральных чисел, где каждое последующее число является суммой трех предыдущих: 1, 1, 1, 3, 5, 9, 17, 31, 57, 105 …

Реализуйте функцию tribonacci() с использованием рекурсии и мемоизации, которая принимает один аргумент:

n — натуральное число
Функция должна возвращать n-й член последовательности Трибоначчи.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию tribonacci(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print(tribonacci(1))
Sample Output 1:

1
Sample Input 2:

print(tribonacci(7))
Sample Output 2:

17
Sample Input 3:

print(tribonacci(4))
Sample Output 3:

3
'''


cache = dict(((1,1),(2,1),(3,1),(4,3)))                # ключ - номер числа, значение - число Фибоначчи

def tribonacci(n):
    result = cache.get(n)
    if result is None:
        result = tribonacci(n - 3) + tribonacci(n - 2)+ tribonacci(n - 1)
        cache[n] = result
    return result
    
print(tribonacci(300))    