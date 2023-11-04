'''
Реализуйте функцию to_binary() с использованием рекурсии, которая принимает один аргумент:

number — неотрицательное целое число
Функция должна возвращать строковое представление числа number в двоичной системе счисления.

Примечание 1. Вспомнить алгоритм перевода числа из десятичной системы счисления в двоичную можно по ссылке.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print(to_binary(15))
Sample Output 1:

1111
Sample Input 2:

print(to_binary(0))
Sample Output 2:

0
Sample Input 3:

print(to_binary(1))
Sample Output 3:

1
'''

# мое решение
def to_binary(number:int,string:str='')->int:
       
    def number_drop(dig:int,res:str)->str:
        if dig==0:
            return res
        elif dig%2==0:
            return number_drop(dig//2,res+'0')
        elif dig%2==1:
            return number_drop(dig//2,res+'1')
        
    if number ==0:
        return 0
    else:
        return number_drop(number,string)
            
#нормальное решение
def to_binary(number):
    if number <= 1:
        return str(number)
    return to_binary(number // 2) + str(number % 2)


# print(to_binary(256))

# list=()




# a = 256 #1111
# print('\n'*3)
# print('=====================')
# print(a%2,a//2)
# print(128%2,128//2)
# print(64%2,64//2)
# print(32%2,32//2)
# print('=====================')