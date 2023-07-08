# Функция is_available_date() 🌶️
# Во время визита очередного гостя сотрудникам отеля приходится проверять, доступна ли та или иная дата для бронирования номера.

# Реализуйте функцию is_available_date(), которая принимает два аргумента в следующем порядке:

# booked_dates — список строковых дат, недоступных для бронирования. Элементом списка является либо одиночная дата, либо период (две даты через дефис). Например:
# ['04.11.2021', '05.11.2021-09.11.2021']
# date_for_booking — одиночная строковая дата или период (две даты через дефис), на которую гость желает забронировать номер. Например:
# '01.11.2021' или '01.11.2021-04.11.2021'
# Функция is_available_date() должна возвращать True, если дата или период date_for_booking полностью доступна для бронирования. В противном случае функция должна возвращать False.

# Примечание 1. Гарантируется, что в периоде левая дата всегда меньше правой.

# Примечание 2. В периоде (две даты через дефис) граничные даты включены.

# Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_available_date(), но не код, вызывающий ее.

from datetime import datetime

def is_available_date(booked_dates, date_for_booking):
    def string_to_date(string_date):
        return datetime.strptime(string_date, '%d.%m.%Y')

    # check if `date_for_booking` is a single date
    if '-' not in date_for_booking:
        date_for_booking = string_to_date(date_for_booking)
        for date_string in booked_dates:
            # check if `date_for_booking` is in range of booked dates
            if '-' in date_string:
                start, end = map(string_to_date, date_string.split('-'))
                if start <= date_for_booking <= end:
                    return False
            else:
                if string_to_date(date_string) == date_for_booking:
                    return False
        return True

    # `date_for_booking` is a period
    else:
        start, end = map(string_to_date, date_for_booking.split('-'))
        for date_string in booked_dates:
            # check if booked dates intersect with `date_for_booking`
            if '-' in date_string:
                booked_start, booked_end = map(string_to_date, date_string.split('-'))
                if start <= booked_end and end >= booked_start:
                    return False
            else:
                if start <= string_to_date(date_string) <= end:
                    return False
        return True

dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '10.11.2021-14.11.2021'
print(is_available_date(dates, some_date))


#ЛУЧШЕЕ РЕШЕНИЕ
from datetime import datetime
def sd(s): # функция превращает строку в дату
    return datetime.strptime(s, '%d.%m.%Y')
def dk(spd): # функция превращает строку c датой или интервалом дат в кортеж из 2 дат
    return (sd(spd[:10]), sd(spd[11:])) if '-' in spd else (sd(spd), sd(spd))
def is_available_date(sp, d):
    for x in sp: # проверяем, пересекаются ли кортежи дат гостя и отеля
        if not(dk(x)[1] < dk(d)[0] or dk(x)[0] > dk(d)[1]):
            return False # если пересекаются, то выводим False
    return True  # а если нет, то True