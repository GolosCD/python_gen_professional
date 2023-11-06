'''
Реализуйте функцию get_value(), которая принимает два аргумента в следующем порядке:

nested_dicts — словарь, содержащий в качестве значений произвольные объекты или словари, которые, в свою очередь, так же содержат в качестве значений произвольные объекты или словари; вложенность может быть произвольной
key — хешируемый объект
Функция должна определять значение, которое соответствует ключу key в словаре nested_dicts или в одном из его вложенных словарей, и возвращать полученный результат.

Примечание 1. Гарантируется, что ключ key присутствует в словаре nested_dicts или в одном из его вложенных словарей, причем в единственном экземпляре.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_value(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

data = {'firstName': 'Тимур', 'lastName': 'Гуев', 'birthDate': {'day': 10, 'month': 'October', 'year': 1993}, 'address': {'streetAddress': 'Часовая 25, кв. 127', 'city': {'region': 'Московская область', 'type': 'город', 'cityName': 'Москва'}, 'postalCode': '125315'}}

print(get_value(data, 'cityName'))
Sample Output 1:

Москва
Sample Input 2:

data = {'first_name': 'Alyson', 'last_name': 'Hannigan', 'birthday': {'day': 24, 'month': 'March', 'year': 1974}}

print(get_value(data, 'birthday'))
Sample Output 2:

{'day': 24, 'month': 'March', 'year': 1974}


'''


def get_value(nested_dicts:dict,key:str)->str:
    try:
        return nested_dicts[key]
    except:
        for val in nested_dicts.values():
            if isinstance(val,dict):
                value = get_value(val,key)
                if value is not None:
                    return value    



data = {'firstName': 'Тимур', 'lastName': 'Гуев', 'birthDate': {'day': 10, 'month': 'October', 'year': 1993}, 'address': {'streetAddress': 'Часовая 25, кв. 127', 'city': {'region': 'Московская область', 'type': 'город', 'cityName': 'Москва'}, 'postalCode': '125315'}}

print(get_value(data, 'cityName'))