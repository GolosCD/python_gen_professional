'''
Функция flatten()
Реализуйте генераторную функцию flatten(), которая принимает один аргумент:

nested_list — список, элементами которого являются целые числа или списки, элементами которых, в свою очередь, 
также являются либо целые числа, либо списки; вложенность может быть произвольной
Функция должна возвращать генератор, порождающий все числа, содержащиеся в nested_list, включая все числа из всех 
вложенных списков, а затем возбуждает исключение StopIteration.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую генераторную функцию flatten(), 
но не код, вызывающий ее.
'''
def flatten(data_list :list):
    for i in data_list:
        if isinstance(i,int):
            yield i
        else:
            yield from flatten(i)
        
generator = flatten([[1, 2], [[3]], [[4], 5]])

print(*generator)        