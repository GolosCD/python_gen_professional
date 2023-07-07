from datetime import datetime

file_name = 'diary.txt'
with open (file_name, 'r', encoding = 'utf8') as open_file:
    raw_file = open_file.readlines()

dates_list:list = ' '.join(raw_file).split("\n \n ")

dates_dict:dict = {datetime.strptime(part[:17],'%d.%m.%Y; %H:%M'):part.replace('\n ','\n') for part in dates_list}


for key in sorted(dates_dict):
    print(dates_dict.get(key))
    print()