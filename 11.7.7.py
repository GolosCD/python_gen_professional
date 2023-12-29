'''
HTML 🌶️
HTML-элементы — основа языка HTML. Каждый HTML-элемент обозначается начальным (открывающим) и конечным (закрывающим) тегами. 
Открывающий и закрывающий теги содержат имя элемента. Открывающий тег может содержать дополнительную информацию — атрибуты и значения атрибутов. 
Гиперссылки в языке HTML создаются с помощью тега <a></a>. Внутрь помещается текст, который будет отображаться на веб-странице. 
Обязательной составляющей тега <a></a> является атрибут href, который задает URL-адрес веб-страницы:

<a href="https://stepik.org">Stepik</a>  
Гиперссылка состоит из двух частей — указателя (Stepik) и адресной части (https://stepik.org). 
Указатель ссылки представляет собой фрагмент текста или изображение, видимые для пользователя. 
Адресная часть ссылки пользователю не видна, она представляет собой адрес ресурса, к которому необходимо перейти. 
Иногда указатель может быть окружен различными тегами (<b></b>, <h1></h1>):

<a href="https://stepik.org"><b><h1>Stepik</h1></b></a>
Напишите программу, которая находит во фрагменте HTML-страницы все гиперссылки и выводит их составляющие — адресные части и указатели.

Формат входных данных
На вход программе подается произвольное количество строк, которые образуют фрагмент HTML-страницы.

Формат выходных данных
Программа должна найти во введенном фрагменте HTML-страницы все гиперссылки и вывести их составляющие — адресные части и указатели, в следующем формате:

<адресная часть>, <указатель>
<адресная часть>, <указатель>
...
Примечание 1. Порядок следования данных об очередной гиперссылке должен совпадать с порядком их следования в введенном фрагменте HTML-страницы.
'''
import re,sys

input_text = [i.strip() for i in sys.stdin]


for i in input_text:
    text = re.findall(r'<a.*?href=\"(.*?)\".*?>(.*?)</a>',i)
    if text:
        print(f'{text[0][0]}, {text[0][1]}')