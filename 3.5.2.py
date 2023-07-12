'''
Пятница, 13-е
Число 
13
13 считалось дьявольским издавна. Это имеет свое объяснение, и не одно: тут есть трактовки, связанные с Тайной вечерей — где были Христос и 
12
12 апостолов, один из которых стал предателем. Есть поверье, что для шабаша нужны 
12
12 ведьм и сатана. В истории число 
13
13 в связке с пятницей стало «несчастливым» в 
1307
1307 году, когда король Франции Филипп Красивый отдал приказ схватить всех тамплиеров — членов рыцарского ордена крестоносцев. Все они были сожжены на кострах инквизиции, и произошло это в пятницу, 
13
13 апреля.

Докажите, что 
13
13-е число месяца чаще всего приходится на пятницу. Напишите программу, которая вычисляет, сколько тринадцатых чисел приходится на каждый день недели в период с 01.01.0001 по 31.12.9999.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести 
7
7 чисел — количество тринадцатых чисел, которые приходятся на понедельник, вторник, среду, четверг, пятницу, субботу и воскресенье в период с 01.01.0001 по 31.12.9999. Числа должны быть расположены каждое на отдельной строке.
'''


#Мое Первое решение

#from datetime import datetime,timedelta
#
#weeks_count = {0:0,1:0,2:0,3:0,4:0,5:0,6:0}
#
#start = datetime.strptime('13.01.0001','%d.%m.%Y')
#
#end = datetime.strptime('14.12.9999','%d.%m.%Y')
#    
#for year in range(1,9999+1):
#    year =str(year).rjust(4,   "0")
#    weeks_count[datetime.strptime(f'13.01.{year}','%d.%m.%Y').weekday()]+=1
#    weeks_count[datetime.strptime(f'13.02.{year}','%d.%m.%Y').weekday()]+=1
#    weeks_count[datetime.strptime(f'13.03.{year}','%d.%m.%Y').weekday()]+=1
#    weeks_count[datetime.strptime(f'13.04.{year}','%d.%m.%Y').weekday()]+=1
#    weeks_count[datetime.strptime(f'13.05.{year}','%d.%m.%Y').weekday()]+=1
#    weeks_count[datetime.strptime(f'13.06.{year}','%d.%m.%Y').weekday()]+=1
#    weeks_count[datetime.strptime(f'13.07.{year}','%d.%m.%Y').weekday()]+=1
#    weeks_count[datetime.strptime(f'13.08.{year}','%d.%m.%Y').weekday()]+=1
#    weeks_count[datetime.strptime(f'13.09.{year}','%d.%m.%Y').weekday()]+=1
#    weeks_count[datetime.strptime(f'13.10.{year}','%d.%m.%Y').weekday()]+=1
#    weeks_count[datetime.strptime(f'13.11.{year}','%d.%m.%Y').weekday()]+=1
#    weeks_count[datetime.strptime(f'13.12.{year}','%d.%m.%Y').weekday()]+=1
#
#
#print(*weeks_count.values(),sep='\n')  

# самое быстрое решение которое я нашел(--- 0.057539939880371094 seconds ---) 
#from datetime import date
#
#days = [0] * 7
#for year in range(1, 10000):
#    for month in range(1, 13):
#        days[date(year=year, month=month, day=13).weekday()] += 1
#
#print(*days, sep='\n')


# Итоговое решение после рефакторинга
from datetime import date
import time

t = time.perf_counter()

days = [0] * 7
    
for year in range(1, 10000):
    days[date(year=year, month=1, day=13).weekday()] += 1
    days[date(year=year, month=2, day=13).weekday()] += 1
    days[date(year=year, month=3, day=13).weekday()] += 1
    days[date(year=year, month=4, day=13).weekday()] += 1
    days[date(year=year, month=5, day=13).weekday()] += 1
    days[date(year=year, month=6, day=13).weekday()] += 1
    days[date(year=year, month=7, day=13).weekday()] += 1
    days[date(year=year, month=8, day=13).weekday()] += 1
    days[date(year=year, month=9, day=13).weekday()] += 1
    days[date(year=year, month=10, day=13).weekday()] += 1
    days[date(year=year, month=11, day=13).weekday()] += 1
    days[date(year=year, month=12, day=13).weekday()] += 1


print(*days,sep='\n')   
print(f"Более разумный перебор:  {time.perf_counter() - t} с.")