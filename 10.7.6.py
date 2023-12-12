'''
Функция nonempty_lines()
Реализуйте генераторную функцию nonempty_lines(), которая принимает один аргумент:

file — название текстового файла, например, data.txt
Функция должна возвращать генератор, порождающий последовательность всех непустых строк файла file с убранным символом переноса строки \n. 
Если строка содержит более 
25 символов, она заменяется многоточием ...

Примечание 1. При открытии файла используйте явное указание кодировки UTF-8.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию nonempty_lines(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:
'''

def nonempty_lines(file :str):

    with open (file,'r',encoding = 'utf-8') as file_raw:
    
        filte_empty_line = (line for line in file_raw.readlines() if len(line)>1)
        
        filter_end_line = (line.strip('\n') for line in filte_empty_line )
        
        filter_25_symbol = ('...' if len(i)>25 else i for i in filter_end_line)
        
        yield from filter_25_symbol
            
            
a = nonempty_lines('nonempty_lines.txt')            


print(next(a))
print(next(a))
print(next(a))
print(next(a))


