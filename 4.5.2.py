from zipfile import ZipFile

total_file_size =0
total_compress_size=0

with ZipFile ('workbook.zip','r') as zip_open:
    zip_read = zip_open.infolist()
    for line in range(len(zip_read)):
        total_file_size+=zip_read[line].file_size
        total_compress_size+=zip_read[line].compress_size

print(f'Объем исходных файлов: {total_file_size} байт(а)')
print(f'Объем сжатых файлов: {total_compress_size} байт(а)')