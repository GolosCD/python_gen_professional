'''
Функция print_digits() 😎
Реализуйте функцию print_digits() с использованием рекурсии, которая принимает один аргумент:

number — натуральное число
Функция должна выводить все цифры числа number, начиная со старших разрядов, каждое на отдельной строке.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию print_digits(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print_digits(12345)
Sample Output 1:

1
2
3
4
5
Sample Input 2:

print_digits(2077)
Sample Output 2:

2
0
7
7
Sample Input 3:

print_digits(8)
Sample Output 3:

8
'''

def print_digits(number):
    
    if number:
        print(str(number)[0])
        print_digits(str(number)[1:])