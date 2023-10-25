'''
Функция get_value()
Реализуйте функцию get_value(), которая принимает три аргумента в следующем порядке:

chainmap — объект типа ChainMap, элементами которого являются словари
key — произвольный объект
from_left — булево значение, по умолчанию равное True
Функция должна возвращать значение по ключу key из chainmap, причем:

если from_left имеет значение True, поиск ключа в chainmap должен происходить от первого словаря к последнему
если from_left имеет значение False, поиск ключа в chainmap должен происходить от последнего словаря к первому
Если ключ key отсутствует в chainmap, функция должна вернуть значение None.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_value(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

print(get_value(chainmap, 'name'))
'''

from collections import ChainMap

def get_value(chainmap:dict, key:str, from_left:str = True):
    if key not in chainmap:
        return None
    elif from_left:
            return chainmap.get(key)
    else:
        for minidict in chainmap.maps[::-1]:
            return minidict.get(key)



       
chainmap = ChainMap({'age': 20}, {'city': 'Moscow'}, {'name': 'Anri', 'age': 20}, {'name': 'Timur', 'age': 29})

print(get_value(chainmap, 'name'))    

