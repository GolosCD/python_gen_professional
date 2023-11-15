import math

def polynom (num:int)->int:
    '''Функция считает квадрат числа и добавляет один, все результаты запуска записываются в коллекцию set'''
    
    #основной расчет
    result = pow(num,2)+1
    
    #создание словаря где значение это коллекция. Именно эта запись позволяет хранить в set больше одного элемента
    polynom.__dict__.setdefault('values',set())
    
    #добавление вычисления в коллекцию
    polynom.__dict__['values'].add(result)
    
    return result
    
polynom(1)
polynom(2)
polynom(3)

print(*sorted(polynom.values))