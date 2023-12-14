'''
Функция unique()
Реализуйте генераторную функцию, которая принимает один аргумент:

iterable — итерируемый объект
Функция должна возвращать генератор, порождающий последовательность элементов итерируемого объекта iterable без дубликатов.

Примечание 1. Элементы итерируемого объекта в возвращаемом функцией генераторе должны располагаться в своем исходном порядке.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию unique(), но не код, вызывающий ее.
'''
from typing import Generator,Any

def unique(sequence :Any) ->Generator:
    result_list :list[Any] = list()
    
    for i in sequence:
        if i in result_list:
            continue
        else:
            result_list.append(i)
    yield from result_list 
    
    
    
    
    
# TEST_4: 
data = map(str.upper, 'jhfjgshgkjfdjsgriyteryowpqerkelfsldfmnmnbmvcnmlgqweootiyoeytkldjhmvxcmkasd')

print(*unique(data))

# J H F G S K D R I Y T E O W P Q L M N B V C X A    


#norm
unique = lambda itr: (i for i in dict.fromkeys(itr))