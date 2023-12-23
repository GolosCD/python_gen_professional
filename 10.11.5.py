'''
Функция group_anagrams()
Анаграммы — это слова, которые состоят из одинаковых букв. Например:

адаптер — петарда
адресочек — середочка
азбука — базука
аистенок — осетинка
Реализуйте функцию group_anagrams(), которая принимает один аргумент:

words — список слов
Функция должна группировать в кортежи слова из списка words, являющиеся анаграммами, и возвращать список полученных кортежей.

Примечание 1. Порядок кортежей в возвращаемом функцией списке, а также порядок элементов в этих кортежах, не важен.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию group_anagrams(), но не код, вызывающий ее.
'''
import itertools as it

def group_anagrams(words :list):
    
    new_words :list = sorted(words,key = lambda x: (len(x),sorted(x)[0]))
    
    my_groups = it.groupby(new_words,key = sorted)
    
    yield from (tuple(gr) for _,gr in my_groups)
    
   
    



# INPUT DATA:
'''
# TEST_1:
groups = group_anagrams(['evil', 'father', 'live', 'levi', 'book', 'afther', 'boko'])

print(*groups)

# TEST_2:
groups = group_anagrams(['evil', 'father', 'book', 'stepik', 'beegeek'])

print(*groups)
'''
# TEST_3:
groups = group_anagrams(['крона', 'сеточка', 'тесачок', 'лучик', 'стоечка', 'норка', 'чулки'])

print(*groups)
'''
# TEST_4:
groups = group_anagrams(['чулки', 'чулки', 'чулки', 'чулки', 'чулки', 'чулки', 'чулки'])

print(*groups)

# TEST_5:
groups = group_anagrams(['beegeek'])

print(*groups)

# TEST_6:
groups = group_anagrams(['клоун', 'отсечка', 'кулон', 'уклон', 'чесотка', 'чулки', 'яяя', 'чулки', 'чесотка', 'яяя'])

print(*groups)

# TEST_7:
groups = group_anagrams(['клоун', 'яяя', 'жжж', 'бббб', 'кулон'])

print(*groups)

# TEST_8:
groups = group_anagrams(['катет', 'кета'])

print(*groups)'''