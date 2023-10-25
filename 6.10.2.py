'''
Функция deep_update()
Реализуйте функцию deep_update(), которая принимает три аргумента в следующем порядке:

chainmap — объект типа ChainMap, элементами которого являются словари
key — хешируемый объект
value — произвольный объект
Функция должна изменять все значения по ключу key во всех словарях в chainmap на value. Если ключ key отсутствует в chainmap, функция должна добавить пару key: value в первый словарь.

Примечание 1. Функция должна изменять передаваемый объект типа ChainMap и возвращать значение None.

Примечание 2. Гарантируется, что передаваемый в функцию объект типа ChainMap содержит хотя бы один словарь.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию deep_update(), но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
'''


from collections import ChainMap

def deep_update(chainmap:dict,key:str,value:str):
    if key not in chainmap.keys():
        chainmap.update({key:value})
    else:    
        for minidict in chainmap.maps:
            if key in minidict:
                minidict[key] = value

#chainmap = ChainMap({'name': 'Tanya'}, {'name': 'Arthur'}, {'name': 'Timur'})

chainmap = ChainMap({'city': 'Moscow'}, {'name': 'Dima'}, {'name': 'Dima'})

deep_update(chainmap, 'name', 'Dima')

print(chainmap)





