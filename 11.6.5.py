'''
Популярность
В онлайн-школе BEEGEEK мы всегда следим за тем, насколько растет наша популярность. 
Для этого мы собираем публикации из различных соцсетей, которые содержат вхождения строки beegeek в нижнем регистре. 
Мы оцениваем публикацию:в 3 балла, если она начинается и заканчивается строкой beegeek
в 2 балла, если она только начинается или только заканчивается строкой beegeek
в 1 балл, если она содержит строку beegeek только внутри
в 0 баллов, если она не содержит строку beegeek
Напишите программу, которая определяет популярность онлайн-школы BEEGEEK путем суммирования баллов всех публикаций.

Формат входных данных
На вход программе подается произвольное число строк, каждая из которых представляет очередную публикацию.

Формат выходных данных
Программа должна определить, во сколько баллов оценивается каждая введенная публикация, и вывести сумму всех полученных баллов.

Примечание 1. Если публикация представляет собой просто строку beegeek, то она оценивается в 
2
2 балла.
'''


import re
import sys

result = 0

for line in [txt.strip() for txt in sys.stdin]:
    tree = 0
    two  = 0
    one  = 0
    zero = 0
    tree += 3 if bool(re.search(r'^beegeek.*beegeek$',line)) else 0      #  3 балла
    two  += 2 if bool(re.search(r'^beegeek',line)) else 0  # 2 балла
    one  += 2 if bool(re.search(r'beegeek$',line)) else 0  # 2 балла
    zero += 1 if bool(re.search(r'beegeek',line)) else 0  # 1 балла
    
    if tree:
        result+= 3
        continue
    elif two or one:
        result+=2
        continue
    elif zero:
        result+=1
        continue
        
         
print (result)


import sys
import re

rating = 0

for line in map(str.rstrip, sys.stdin):
    if re.fullmatch(r'beegeek.*beegeek', line):
        rating += 3
    elif re.fullmatch(r'^beegeek.*|.*beegeek$', line):
        rating += 2
    elif re.fullmatch(r'.+beegeek.+', line):
        rating += 1
        
print(rating)