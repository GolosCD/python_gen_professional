'''
Напишите программу, которая переопределяет встроенную функцию print() так, чтобы она печатала все переданные строковые аргументы в верхнем регистре.

Примечание 1. Значения sep и end также должны переводиться в верхний регистр.
'''

#re-assigning the function print
import builtins as b

#new function print
def print (*args,sep=' ', end='\n')->str:
    '''my new print feature. this function outputs all elements in uppercase'''

    args_upper = [i.upper() if isinstance(i,str) else i for i in args]

    b.print(args_upper,sep=sep.upper(),end=end.upper())










# TEST_1:
print('beegeek', [1, 2, 3], 4)

# TEST_2:
print('bee', 'geek', sep=' and ', end=' wow')

# TEST_3:
words = ('black', 'white', 'grey', 'black-1', 'white-1', 'python')
print(*words, sep=' to ', end=' LOVE')

# TEST_4:
words = [['black', 'white', 'grey', 'black-1', 'white-1', 'python']]
print(*words, sep=' to ', end=' LOVE')

# TEST_5:
words = ['a', 2, 'b', 3, ['1a', '2a', '3a', '4a'], '5A', True, 8.763, ('python', 'c++')]
print(*words)

# # TEST_6:
words = ['a', 2, 'b', 3, ['1a', '2a', '3a', '4a'], '5A', True, 8.763, ('python', 'c++')]
kwarg = {'sep' : ' ', 'end' : ' Finish'}
print(*words, **kwarg)

# # TEST_7:
words = ['a', 2, 'b', 3, ['1a', '2a', '3a', '4a'], '5A', True, 8.763, ('python', 'c++')]
kwarg = {'sep' : ',f ', 'end' : ' Finish'}
print(*words, **kwarg)