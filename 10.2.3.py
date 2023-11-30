'''
Реализуйте функцию get_min_max(), которая принимает один аргумент:

data — список произвольных объектов, сравнимых между собой
Функция должна возвращать кортеж, в котором первым элементом является индекс минимального элемента в списке data,
вторым — индекс максимального элемента в списке data. Если список data пуст, функция должна вернуть значение None.

Примечание 1. Если минимальных / максимальных элементов несколько, следует вернуть индексы первого по порядку элемента.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_min_max(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

data = [2, 3, 8, 1, 7]

print(get_min_max(data))
Sample Output 1:

(3, 2)
Sample Input 2:

data = [1, 1, 2, 3, 8, 8]

print(get_min_max(data))
Sample Output 2:

(0, 4)
Sample Input 3:

data = [9]

print(get_min_max(data))
Sample Output 3:

(0, 0)
'''

def get_min_max(data :list[int]) ->tuple[int]:
    
    if not data:
        return None
    
    return tuple((data.index(min(data)),data.index(max(data))))




data = [2, 3, 8, 1, 7]

print(get_min_max(data))