'''
Реализуйте функцию get_min_max(), которая принимает один аргумент:

iterable — итерируемый объект, элементы которого сравнимы между собой
Функция должна возвращать кортеж, в котором первым элементом является минимальный элемент итерируемого объекта iterable, 
вторым — максимальный элемент итерируемого объекта iterable. Если итерируемый объект iterable пуст, функция должна вернуть значение None.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_min_max(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

iterable = iter(range(10))

print(get_min_max(iterable))
Sample Output 1:

(0, 9)
Sample Input 2:

iterable = [6, 4, 2, 33, 19, 1]

print(get_min_max(iterable))
Sample Output 2:

(1, 33)
Sample Input 3:

iterable = iter([])

print(get_min_max(iterable))
Sample Output 3:

None
'''

def get_min_max(iterable): 

    try:
        mi = mx = next(iter(iterable))
    except StopIteration:
        return None
        
    for i in iterable:    
        if i<mi:
            mi=i
        elif mx<i:
            mx=i
    return tuple((mi,mx)) 