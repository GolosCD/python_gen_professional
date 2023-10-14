'''
У Тимура имеется немало друзей из других городов или стран, которые часто приезжают к нему в гости с целью увидеться и развлечься. Чтобы не забыть ни об одной встрече, Тимур записывает имена и фамилии друзей в csv файл, дополнительно указывая для каждого дату и время встречи. Вам доступен этот файл, имеющий название meetings.csv, в котором в первом столбце записана фамилия, во втором — имя, в третьем — дата в формате DD.MM.YYYY , в четвертом — время в формате HH:MM:

surname,name,meeting_date,meeting_time
Харисов,Артур,15.07.2022,17:00
Геор,Гагиев,14.12.2022,18:00
...

Напишите программу, которая выводит фамилии и имена друзей Тимура, предварительно отсортировав их по дате и времени встречи от самой ранней до самой поздней. Фамилии и имена должны быть расположены каждые на отдельной строке.

Примечание 1. Начальная часть ответа выглядит так:

Гудцев Таймураз
Харисов Артур
Базиев Герман
...

Примечание 2. Гарантируется, что никакие две встречи не имеют одновременно одинаковые даты и время.

Примечание 3. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.

Примечание 4. Разделителем в файле meetings.csv является запятая, при этом кавычки не используются.

Примечание 5. При открытии файла используйте явное указание кодировки UTF-8.

'''

from collections import namedtuple
from datetime import datetime
import csv

field_name_value:list = list(['surname', 'name', 'meeting_date', 'meeting_time']);

Friend:namedtuple = namedtuple('Friend',field_name_value);

friend_dicts:list = list();

with open ('meetings.csv','r',encoding='utf8') as file_open:
    for friend_dict in csv.DictReader(file_open,delimiter=','):

        current_friend = Friend(*friend_dict.values());

        friend_dicts.append(current_friend);
        
sortedtuples:list = sorted(friend_dicts,key=lambda x: (datetime.strptime(x.meeting_date,'%d.%m.%Y'), datetime.strptime(x.meeting_time,'%H:%M')));

for friend in sortedtuples:

    print(friend.surname,friend.name);