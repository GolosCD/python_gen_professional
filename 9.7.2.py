'''
Напишите программу с использованием декоратора, которая переопределяет функцию print() так, чтобы она печатала весь текст в верхнем регистре.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна задекорировать функцию print() так, чтобы она печатала весь текст в верхнем регистре.

Примечание 1. Значения sep и end также должны переводиться в верхний регистр.

Примечание 2. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
'''

import builtins as b

def print_decorator(func):

    def upper_cases (*args,sep = ' ',end = '\n'):
    
        upper_args = [i.upper() if isinstance(i,str) else i for i in args]
        
        b.print(*upper_args,sep=sep.upper(),end = end.upper())
        
    return upper_cases
    
print = print_decorator(print)

    




# INPUT DATA:

# TEST_1:
print('hi', 'there', end='!')

# TEST_2:

print('are you in trouble?')

# TEST_3:
print(111, 222, 333, sep='xxx')

# TEST_4:
print(111, 222, 333, sep='xxx', end='python')
print(111, 222, 333, sep='--', end='\n')
print(111, 222, 333, sep='qqq', end='!')

# TEST_5:
print('aaa', 'bbb', 'CCC', sep='xxx', end='stepik')
print('aaa', 'bbb', 'CCC', sep='--', end='python')
print('aaa', 'bbb', 'CCC', sep='qqq', end='!')