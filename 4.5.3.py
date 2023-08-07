from zipfile import ZipFile

best = 1000
name = ''

with ZipFile ('workbook.zip','r') as zip_open:
    zip_read = zip_open.infolist()
    for line in range(len(zip_read)):
        if zip_read[line].compress_size!=0 and zip_read[line].file_size!=0:
            a=(zip_read[line].compress_size/zip_read[line].file_size)
            if a<best:
                best = min (a,best)
                name = zip_read[line].filename.split('/')[-1]
        

print(name)
