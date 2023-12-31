Реализуйте функцию get_biggest(), которая принимает один аргумент:

numbers — список целых неотрицательных чисел
Функция должна возвращать наибольшее число, которое можно составить из чисел из списка numbers. Если список numbers пуст, функция должна вернуть число 
−
1
−1.

Примечание 1. Рассмотрим первый тест со списком чисел [1, 2, 3], из которых можно составить следующие числа:
123
,
132
,
213
,
231
,
312
,
321
123,132,213,231,312,321
Наибольшим из представленных является 
321
321.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_biggest(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

def get_biggest(n_list: list):
    if n_list:
        result = ''
    
        amount_dig_max_el = int(max(n_list, key = lambda x: len(str(x))))
    
        n_list.sort(key=lambda x: str(x)*amount_dig_max_el,reverse=True)
        for num in n_list:
            result+=str(num)
        
        return int(result)
    return -1



