'''
Реализуйте функцию verification(), которая проверяет правильность введенного пароля. Она должна принимать четыре аргумента в следующем порядке:

login — логин пользователя
password — пароль пользователя
success — некоторая функция
failure — некоторая функция
Пароль считается правильным, если в нем присутствует, хотя бы одна заглавная латинская буква, хотя бы одна строчная латинская буква и хотя бы одна цифра. Функция verification() должна вызывать функцию success() с аргументом login, если переданный пароль является правильным, иначе — функцию failure() с аргументами login и строкой-сообщением об ошибке:

в пароле нет ни одной буквы, если в пароле отсутствуют латинские буквы
в пароле нет ни одной заглавной буквы, если в пароле отсутствуют заглавные латинские буквы
в пароле нет ни одной строчной буквы, если в пароле отсутствуют строчные латинские буквы
в пароле нет ни одной цифры, если в пароле отсутствуют цифры
Примечание 1. Если пароль не удовлетворяет нескольким условиям, то приоритеты выбора строки-сообщения об ошибке являются следующими:

в пароле нет ни одной буквы
в пароле нет ни одной заглавной буквы
в пароле нет ни одной строчной буквы
в пароле нет ни одной цифры
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию verification(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

def success(login):
    print(f'Привет, {login}!')

def failure(login, text):
    print(f'{login}, попробуйте снова. Ошибка: {text}')

verification('timyrik20', 'Beegeek314', success, failure)
Sample Output 1:

Привет, timyrik20!
Sample Input 2:

def success(login):
    print(f'Здравствуйте, {login}!')

def failure(login, text):
    print(f'{login}, попробуйте снова. Текст ошибки: {text}')

verification('Ruslan_Chaniev', 'stepikstepik2', success, failure)
Sample Output 2:

Ruslan_Chaniev, попробуйте снова. Текст ошибки: в пароле нет ни одной заглавной буквы
'''

#МОЕ ПЕРВОЕ РЕШЕНИЕ - ОЧЕНЬ ПЛОХОЕ, ПОЭТОМУ Я ПОШЕЛ ДАЛЬШЕ
import string

def verification(login   :str,
                 password:str,
                 success:callable,
                 failure:callable
                 )->list:
    flag = False

    if any(i.isalpha() for i in password if i.lower() in string.ascii_lowercase):
        if any(i.isupper() for i in password if i in string.ascii_uppercase):
                if any(i.lower() for i in password if i in string.ascii_lowercase):
                        if any(i.isdigit() for i in password):
                            flag = True
                        else:
                            failure(login,'в пароле нет ни одной цифры') 
                else:
                    failure(login,'в пароле нет ни одной строчной буквы')
        else:
            failure(login,'в пароле нет ни одной заглавной буквы')
    else:
        failure(login,'в пароле нет ни одной буквы')      

    if flag:
        success(login)

#Затемя я переломапатил решений 20 и собрал все лучшие что нашел и получилось вот такое решение.        
from string import ascii_letters, ascii_uppercase, ascii_lowercase, digits

def verification(login   :str,
                 password:str,
                 success :callable,
                 failure :callable
                 )->str:
    
    #создали словарь где ключ - это набор символов которые нужно проверить
    error_dict:dict = dict(((ascii_letters,'буквы'),
                            (ascii_uppercase,'заглавной буквы'),
                            (ascii_lowercase,'строчной буквы'),
                            (digits,'цифры')))
    #функция которая берет пароль и сверяет его с ключом словаря. Но не посимвольно, а сразу чере спец метод set'ов
    check_simbol = lambda my_password,sequence: set(my_password).isdisjoint(sequence)
    
    for key in error_dict:
         if check_simbol(password,key):
              failure(login,f'в пароле нет ни одной {error_dict.get(key)}')
              break
    else:
         success(login)

#тот же смысл только без лямбда функции, теперь решение читается как просто книжка
from string import ascii_letters, ascii_uppercase, ascii_lowercase, digits

def verification(login   :str,
                 password:str,
                 success :callable,
                 failure :callable
                 )->str:
    
    #создали словарь где ключ - это набор символов которые нужно проверить
    error_dict:dict = dict(((ascii_letters,'буквы'),
                            (ascii_uppercase,'заглавной буквы'),
                            (ascii_lowercase,'строчной буквы'),
                            (digits,'цифры')))
    
    for key in error_dict:
         if set(password).isdisjoint(key):
              failure(login,f'в пароле нет ни одной {error_dict.get(key)}')
              break
    else:
         success(login)         