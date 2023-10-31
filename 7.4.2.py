'''
В онлайн-школе BEEGEEK имя ученика считается корректным, если оно начинается с заглавной латинской буквы, за которой следуют строчные латинские буквы. Например, имена Timur и Yo считаются корректными, а имена timyrik, Yo17, TimuRRR нет. Также у каждого ученика имеется идентификационный номер, представленный натуральным числом, который выдается при поступлении в школу. К примеру, если в школе обучается 
10
10 учеников, то новый прибывший ученик получит идентификационный номер равный 
11
11.

Реализуйте функцию get_id(), которая принимает два аргумента:

names — список имен учеников, обучающихся в школе
name — имя поступающего ученика
Функция должна возвращать идентификационный номер, который получит поступающий в школу ученик, при этом

если имя ученика name не является строкой (тип str), функция должна возбуждать исключение:
TypeError('Имя не является строкой')
если имя ученика name является строкой (тип str), но не представляет собой корректное имя, функция должна возбуждать исключение:
ValueError('Имя не является корректным')
Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_id(), но не код, вызывающий ее. 

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

names = ['Timur', 'Anri', 'Dima']
name = 'Arthur'

print(get_id(names, name))
'''


import string

#мое первое решение
# def get_id (names:list, name:str)->int:

    #список запрещенных символов
    # bad_symb:str = list(string.printable[:10]+string.printable[36:])
    
    #вычисленеи нового ID
    # new_id:int = len(names)+1
    
    # if not isinstance(name,str):
        # raise TypeError('Имя не является строкой')
        
    # if not name[0].isupper():
        # raise ValueError('Имя не является корректным')
    
    # check_al1:bool = min([False if i in name[1:] else True for i in bad_symb])
    
    # if not check_al1:
        # raise ValueError('Имя не является корректным')
        
    # return  new_id  
    
# names = ['Timur', 'Anri', 'Dima']
# name = 'Arthur'

# print(get_id(names, name))

def get_id (names:list, name:str)->int:
    
    #вычисленеи нового ID
    new_id:int = len(names)+1
    
    if not isinstance(name,str):
        raise TypeError('Имя не является строкой')
        
    if not (name[0].isupper() and name[1:].islower() and name.isalpha()):
        raise ValueError('Имя не является корректным')

    return  new_id  
    
names = ['Timur', 'Anri', 'Dima']
name = 'Arthur'

print(get_id(names, name))