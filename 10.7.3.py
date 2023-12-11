'''
Функция filter_names()
Реализуйте генераторную функцию filter_names(), которая принимает три аргумента в следующем порядке:

names — список имен
ignore_char — одиночный символ
max_names — натуральное число
Функция должна возвращать генератор, порождающий max_names имён из списка names, игнорируя имена, которые

начинаются на ignore_char (в любом регистре)
содержат хотя бы одну цифру
Если max_names больше количества имен в списке names, то генератор должен породить все возможные имена из данного списка. 

Примечание 1. Имена в возвращаемом функцией генераторе должны располагаться в своем исходном порядке.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию filter_names(), но не код, вызывающий ее.
'''


def filter_names(names :list[str], ignore_char :str, max_names :int) -> list[str]:
    filter_1 = (name for name in names if not name.lower().startswith(ignore_char.lower()))
    
    filter_2 = (i for i in filter_1 if all(map(lambda x: x.isalpha(),i.split())) )
    
    filter_3 = (i for i,v in zip(filter_2,range(max_names)))

    yield from filter_3
        


# data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']

# print(*filter_names(data, 'D', 3))

data = ['Di6ma', 'Ti4mur', 'Ar5thur', 'Anri7620', 'Ar3453ina', '345German', 'Ruslan543', 'Soslanfsdf123', 'Geo000000r']

print(*filter_names(data, 'A', 100))


data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']

print(*filter_names(data, 't', 20))