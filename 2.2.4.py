""" Дана последовательность неотрицательных целых чисел. Напишите программу, которая выводит те числа, которые встречаются в данной последовательности более одного раза.

Формат входных данных
На вход программе подается строка, содержащая целые неотрицательные числа, разделенные пробелом.

Формат выходных данных
Программа должна вывести те числа, которые встречаются в данной строке более одного раза, разделяя их пробелом. Числа должны быть расположены в порядке возрастания и не должны повторяться.

Примечание 1. Если повторяющихся чисел в исходной строке нет, программа ничего не должна выводить.

Примечание 2. Тестовые данные доступны по ссылкам: """


a = '3 1 3 2 3 11 4 3 5 3 6 3 7 3 8 3 9 3 10 3 11 3 3 12 13 1'

my_range: list = [i for i in a.split()]

print(*sorted(set(filter(lambda x: my_range.count(x)>1,my_range)),key=lambda x: int(x)))