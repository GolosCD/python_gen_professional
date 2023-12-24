'''
Перестановки
Напишите программу, которая выводит все перестановки символов строки без дубликатов.

Формат входных данных
На вход программе подается произвольная строка из строчных латинских букв, длина которой не превышает 
10
10 символов.

Формат выходных данных
Программа должна вывести все перестановки символов данной строки без дубликатов в алфавитном порядке, каждую на отдельной строке.

Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

aab
Sample Output 1:

aab
aba
baa
Sample Input 2:

abc
Sample Output 2:

abc
acb
bac
bca
cab
cba
Sample Input 3:

ab
Sample Output 3:

ab
ba
Sample Input 4:

a
Sample Output 4:

a
'''


import itertools as it

input_list :list = 'aaaaabbbbb'

input_set = set(it.permutations(input_list))

for i in sorted(input_set):
    print(''.join(i))
