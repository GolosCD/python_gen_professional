'''
Реализуйте функцию is_palindrome() с использованием рекурсии, которая принимает один аргумент:

string — произвольная строка
Функция должна возвращать значение True, если переданная строка является палиндромом, или False в противном случае.

Примечание 1. Палиндром — текст, одинаково читающийся в обоих направлениях.

Примечание 2. Пустая строка является палиндромом, как и строка, состоящая из одного символа.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_palindrome(), но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:
'''

def is_palindrome(string:str)->bool:
    def revers_palindom(revstr:str)->bool:
        if string==revstr and string[1]==revstr[-2] :
            return True
        else:
            return False
    if len(string)==1 or string=='':
        return True
    else:    
        return revers_palindom(string[-1]+string[1:-1]+string[0])
    



print(is_palindrome('abcca'))