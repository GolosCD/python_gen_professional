'''
Назовем пароль хорошим, если

его длина равна 
9
9 или более символам
в нем присутствуют большие и маленькие буквы любого алфавита
в нем имеется хотя бы одна цифра
Реализуйте функцию is_good_password() в стиле LBYL, которая принимает один аргумент:

string — произвольная строка
Функция должна возвращать True, если строка string представляет собой хороший пароль, или False в противном случае.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_good_password(), но не код, вызывающий ее. 

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print(is_good_password('41157082'))
Sample Output 1:

False
Sample Input 2:

print(is_good_password('мойпарольсамыйлучший'))
Sample Output 2:

False
Sample Input 3:

print(is_good_password('МойПарольСамыйЛучший111'))
Sample Output 3:

True
'''

def is_good_password(string:str)-> bool:
    if all([(any(i.islower() for i in string) and any(i.isupper() for i in string)),any(i.isdigit() for i in string),len(string)>=9]):
        return True
    else:
        return False


