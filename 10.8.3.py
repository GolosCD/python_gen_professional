'''
Функция alnum_sequence()
Реализуйте функцию alnum_sequence(), которая не принимает никаких аргументов.

Функция должна возвращать итератор, циклично генерирующий бесконечную последовательность натуральных чисел и заглавных латинских букв:
1
,
�
,
2
,
�
,
3
,
�
,
.
.
,
�
,
25
,
�
,
26
,
�
1,A,2,B,3,C,..,X,25,Y,26,Z

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию alnum_sequence(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

alnum = alnum_sequence()

print(*(next(alnum) for _ in range(55)))
Sample Output 1:

1 A 2 B 3 C 4 D 5 E 6 F 7 G 8 H 9 I 10 J 11 K 12 L 13 M 14 N 15 O 16 P 17 Q 18 R 19 S 20 T 21 U 22 V 23 W 24 X 25 Y 26 Z 1 A 2
Sample Input 2:

alnum = alnum_sequence()

print(*(next(alnum) for _ in range(100)))
Sample Output 2:

1 A 2 B 3 C 4 D 5 E 6 F 7 G 8 H 9 I 10 J 11 K 12 L 13 M 14 N 15 O 16 P 17 Q 18 R 19 S 20 T 21 U 22 V 23 W 24 X 25 Y 26 Z 1 A 2 B 3 C 4 D 5 E 6 F 7 G 8 H 9 I 10 J 11 K 12 L 13 M 14 N 15 O 16 P 17 Q 18 R 19 S 20 T 21 U 22 V 23 W 24 X
'''



import itertools as it

from string import ascii_uppercase


def alnum_sequence():
    a = it.cycle(ascii_uppercase)
    b = it.cycle(range(1,len(ascii_uppercase)+1))
    
    for i in it.count():
        yield next(b)
        yield next(a)




alnum = alnum_sequence()

print(*(next(alnum) for _ in range(55)))