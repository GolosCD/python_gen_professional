# расчет времени работы магазина
from datetime import datetime, timedelta

day,time= '16.07.2022 18:00'.split(' ')

day = datetime.strptime(day,'%d.%m.%Y')

time = datetime.strptime(time,'%H:%M')


work = [('10:00', '18:00'),
        ('09:00', '21:00'),
        ('09:00', '21:00'),
        ('09:00', '21:00'),
        ('09:00', '21:00'),
        ('09:00', '21:00'),
        ('10:00', '18:00')]


start = datetime.strptime(work[int(day.strftime('%w'))][0],'%H:%M')

end = datetime.strptime(work[int(day.strftime('%w'))][1],'%H:%M')

if start<=time<end:
    print(((end-start).seconds-(time-start).seconds)//60 ,start,end)
else:
    print('Магазин не работает')
    
from datetime import datetime
date = datetime.strptime(input(), '%d.%m.%Y %H:%M')

start, end = (date.replace(hour=i, minute=0) for i in ((9, 21), (10, 18))[date.weekday() > 4])

if start <= date < end:
    print((end - date).seconds // 60)
else:
    print('Магазин не работает')    
