'''
Строка запроса (query string) — часть URL адреса, содержащая ключи и их значения. Она начинается после вопросительного знака и идет до конца адреса. Например:

https://beegeek.ru?name=timur     # строка запроса: name=timur
Если параметров в строке запроса несколько, то они отделяются символом амперсанда &:

https://beegeek.ru?name=timur&color=green     # строка запроса: name=timur&color=green 
Реализуйте функцию sourcetemplate(), которая принимает один аргумент:

url — URL адрес
Функция sourcetemplate() должна возвращать функцию, которая принимает произвольное количество именованных аргументов и возвращает url адрес, объединенный со строкой запроса, сформированной из переданных аргументов. При вызове без аргументов она должна возвращать исходный url адрес без изменений.

Примечание 1. Параметры в строке запроса должны располагаться в лексикографическом порядке ключей.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию sourcetemplate(), но не код, вызывающий ее.

'''

def sourcetemplate(adress:str)->callable:
    def power_ranger(**kwargs)->str:
        param_lists:list = [[f'{key}={val}' for key, val in sorted(kwargs.items())]]
        return f'{adress}?{"&".join(*param_lists)}' if kwargs else adress
    return power_ranger    

# INPUT DATA:

# TEST_1:
url = 'https://beegeek.ru'
load = sourcetemplate(url)
print(load(name='timur'))

# TEST_2:
url = 'https://stepik.org/lesson/651459/step/14'
load = sourcetemplate(url)
print(load(thread='solutions', unit=648165))

# TEST_3:
url = 'https://beegeek.ru'
load = sourcetemplate(url)
print(load())

# TEST_4:
url = 'https://all_for_comfort_life.com'
load = sourcetemplate(url)
print(load(smartphone='iPhone', notebook='huawei', sale=True))
#https://all_for_comfort_life.com?notebook=huawei&sale=True&smartphone=iPhone

# TEST_5:
url = 'https://hide_and_seek.harvard'
load = sourcetemplate(url)
print(load(wizard='Dambldor', magic_wand='elderberry', thief='Volandemord'))