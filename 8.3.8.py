'''
Реализуйте функцию is_power() с использованием рекурсии, которая принимает один аргумент:

number — натуральное число
Функция должна возвращать значение True, если number является степенью числа 
2
2, или False в противном случае.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_power(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print(is_power(512))
Sample Output 1:

True
Sample Input 2:

print(is_power(15))
Sample Output 2:

False
Sample Input 3:

print(is_power(1))
Sample Output 3:

True
'''




#Мое решение
def is_power(number:int)->bool:
    def get_pow(a:int)->int:
        if number==1 or number ==a :
            return True
        elif a<=number:
            return get_pow(a*2)
        else:
            return False
    return get_pow(2)        
            
# не мое но более понятное            
def is_power(number: int, ch = 2) -> bool:
    if number == 1 or number == ch:
        return True
    else:
        if ch <= number:
            return is_power(number, ch*2)
        else:
            return False
    
print(is_power(512))                
    