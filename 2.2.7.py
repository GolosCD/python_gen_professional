Схожие слова
Напишите программу, которая находит все схожие слова для заданного слова. Слова называются схожими, если имеют одинаковое количество и расположение гласных букв. При этом сами гласные могут различаться.

Формат входных данных
На вход программе подается одно слово, записанное в первой строке, затем натуральное число 
�
n — количество слов для сравнения и 
�
n строк со словами.

Формат выходных данных
Программа должна вывести все схожие слова для заданного слова, сохранив их исходный порядок следования.

Примечание 1. После последней гласной в начальном и проверяемом слове может быть любое количество согласных.

Примечание 2. В русском языке 
10
10 гласных букв (а, у, о, ы, и, э, я, ю, ё, е) и 
21
21 согласная буква (б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ).

Примечание 3. Тестовые данные доступны по ссылкам:

vov = ('а, у, о, ы, и, э, я, ю, ё, е')
slovo = [i for i, letter in enumerate(input()) if letter in vov]
my_list_word = [input() for _ in range(int(input()))]           


my_dict = dict()

for word in my_list_word:
    word_ind = [i for i, letter in enumerate(word) if letter in vov]

    if word_ind == slovo:
        print(word)
        
        
#vov = ('а, у, о, ы, и, э, я, ю, ё, е')
#slovo = [i for i, letter in enumerate(input()) if letter in vov]
#for _ in range(int(input())):
#    word = input()
#    if [i for i, letter in enumerate(word) if letter in vov]== slovo:
#        print(word)
        