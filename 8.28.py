'''
Реализуйте функцию print_digits() с использованием рекурсии, которая принимает один аргумент:

number — натуральное число
Функция должна выводить все цифры числа number, начиная с младших разрядов, каждое на отдельной строке.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию print_digits(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print_digits(12345)
Sample Output 1:

5
4
3
2
1
Sample Input 2:

print_digits(7)
Sample Output 2:

7
'''
# мое позорное решение
def print_digits(num:int)->int:
        if num<10:
            print(num)
        else:
            print (num%10)
            print_digits(int(str(num)[:len(str(num))-1]))    


print_digits(8)

# нормальное решение
def print_digits(number):
    if number:
        print(number % 10)
        print_digits(number//10)