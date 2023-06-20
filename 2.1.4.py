Реализуйте функцию print_given(), которая принимает произвольное количество позиционных и именованных аргументов и выводит все переданные аргументы, указывая тип каждого. Пары аргумент-тип должны выводиться каждая на отдельной строке, в следующем формате:

для позиционных аргументов:
<значение аргумента> <тип аргумента>
для именованных аргументов:
<имя переменной> <значение аргумента> <тип аргумента>
Примечание 1. При выводе позиционные аргументы должны быть расположены в порядке их передачи, именованные — в лексикографическом порядке имен переменных.

Примечание 2. При выводе сначала должны следовать все позиционные аргументы, затем — все именованные.

Примечание 3. Если в функцию ничего не передается, функция ничего не должна выводить.

Примечание 4. В тестирующую систему сдайте программу, содержащую только необходимую функцию print_given(), но не код, вызывающий ее.

Примечание 5. Тестовые данные доступны по ссылкам:

def print_given(*args,**kwargs):

    for val in args:
        print(f'{val} {type(val)}')
        
    for key in sorted(kwargs):
        val = kwargs.get(key)
        print( f'{key} {val} {type(val)}')