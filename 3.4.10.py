''''
Реп по матеше
Репетитор по математике проводит занятия по 
45
45 минут с перерывами по 
10
10 минут. Репетитор обозначает время начала рабочего дня и время окончания рабочего дня. Напишите программу, которая генерирует и выводит расписание занятий.

Формат входных данных
На вход программе в первой строке подается время начала рабочего дня в формате HH:MM. В следующей строке вводится время окончания рабочего дня в том же формате.

Формат выходных данных
Программа должна сгенерировать и вывести расписание занятий. На первой строке выводится время начала и окончания первого занятия в формате HH:MM - HH:MM, на второй строке — время начала и окончания второго занятия в том же формате, и так далее.

Примечание 1. Если занятие обрывается временем окончания работы, то добавлять его в расписание не нужно.

Примечание 2. Если разница между временем начала и окончания рабочего дня меньше 
45
45 минут, программа ничего не должна
'''


from datetime import datetime,timedelta

def scheduler(start,end):   
    if (end-start).seconds>=2700:
        str_list: list = list()
        end_list: list = list()
        
        str_list.append(st)
        end_list.append(st+timedelta(minutes=45))

        while max(end_list)!=end\
              and ((end-(max(end_list)+timedelta(minutes=10))).seconds>=2700\
              and max(end_list)+timedelta(minutes=54)<end):
            
            str_list.append(max(end_list)+timedelta(minutes=10))
            end_list.append(max(str_list)+timedelta(minutes=45))
        return [f'{s.strftime("%H:%M")} - {e.strftime("%H:%M")}' for s,e in zip(str_list,end_list)]
    else:
        pass
        
part = '%H:%M'        

st = datetime.strptime(input(),part)

en = datetime.strptime(input(),part)

a =scheduler(st,en)
if a:
    print(*a ,sep='\n')
    
    
from datetime import datetime, timedelta
f = '%H:%M'
start, stop = (datetime.strptime(input(), f) for i in '__')
while start <= (stop - timedelta(minutes=45)):
    print(start.strftime(f), '-', (start + timedelta(minutes=45)).strftime(f))
    start += timedelta(minutes=55)    