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

from datetime import datetime,date
def is_available_date(booked_dates: str,
                      date_for_booking: str):
    #booked_dates_dict = [datetime.strptime(day,'%d.%m.%Y').timestamp() for date in booked_dates for day in date.split('-')]
    booked_dates_list: list = [[int(datetime.strptime(day,'%d.%m.%Y').timestamp()) for day in date.split('-') ]for date in booked_dates]
    
    booked_dates_set: set = set()

    for date_time in booked_dates_list:
        for date_day in range(min(date_time)/86400,max(date_time)+1/86400):
            booked_dates_set.add(datetime.fromtimestamp(float(date_day)).strftime('%d/%m/%y'))

    date_for_booking_list: list = [[int(datetime.strptime(day,'%d.%m.%Y').timestamp()) for day in date_for_booking.split('-') ]]
    
    date_for_booking_set: set = set()  

    for date_time in date_for_booking_list:
        for date_day in range(min(date_time),max(date_time)+1):
            date_for_booking_set.add(datetime.fromtimestamp(float(date_day)).strftime('%d/%m/%y'))

    #return booked_dates_set.isdisjoint(date_for_booking_set)
    return sorted(booked_dates_set),sorted(date_for_booking_set)
    #return booked_dates_list,date_for_booking_list

dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '10.11.2021-14.11.2021'
print(is_available_date(dates, some_date))