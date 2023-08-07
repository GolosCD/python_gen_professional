from zipfile import ZipFile

from datetime import datetime

format_date = '%Y-%m-%d %H:%M:%S'

date_check = datetime.strptime('2021-11-30 14:22:00',format_date)

result = list()

with ZipFile ('workbook.zip','r') as zip_open:

    zip_read = zip_open.infolist()
    
    for line in range(len(zip_read)):
        file_date = datetime(*zip_read[line].date_time)
        
        if file_date>date_check and zip_read[line].filename.split('/')[-1]!='':
            result.append(zip_read[line].filename.split('/')[-1])
        

print(*sorted(result),sep='\n')
