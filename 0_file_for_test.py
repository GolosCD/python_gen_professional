# print(bool([]))

# print(bool({}))

# print(bool({0: False}))

# print(bool(False))

# print(bool('False'))

# print(bool(''))

# print(bool(()))

# print(bool(set()))

# print(bool([0, 0, 0]))

# print(bool(0.0))

# print(bool(True))

# print(bool(0))

# print(bool(None))

# objects = [0, [False], '0', False, True, [], 'bee']

# true_objects = filter(None, objects)

# print(*true_objects)

# print('\n'*5)

# data = ['Timur', -16.648911695768902, 'six', -202, 883.0093275936454, -765, (3, 4), -105.10718000213546, 976, -308.96857946288094, 458, ['one', 'two'], 479.92207220345927, -87, -71, 'twelve', 112, -621, -715.0179551194733, 'seven', 229, 729, -358, [1, 2, 3], -974, 882, -894.4709033242768, '', 323.7720806756133, 'beegeek', -224, 431, 170.6353248658936, -343.0016746052049, 'number', 104.17133679352878, [], -353.5964777099863, 'zero', -113, 288, None, -708.3036176571618]


# print(*map(int,filter(lambda x: x if isinstance(x,int) or isinstance(x,float) else 0,data)),sep='\n')

# print('\n'*5)

# numbers = [4754, -4895, -364, -4764, 4683, 1639, -43, 228, -2701, -1503, 1223, 4340, -1296, 3939, -345, 623, -3275, 1003, 4367, -1739, 550, -1217, -1334, 1526, -4359, -3028, -4663, 3356, 3887, 4297, -1982, 1013, 3299, 3556, -3324, 417, 3531, -3134, 1782, 4439, 1652, -985, 4327, 1517, 1225, -915, 2808, -3851, -1005, 3396, 2842, -3879, -3824, -3805, 1609, -4741, -3072, 3573, 4680, 588, -1430, 2378, -1095, -343, 4357, -2164, -3304, 4354, 4926, -352, -1187, -3313, 2741, 4786, -2689, 741, 4558, 1442, 62, -1099, -2201, -16, -3115, 1862, 2384, 4072, -90, 204, 1158, -3134, -2512, 756, 4148, 4370, 1756, 3609, -1148, -3909, 4123, -2906, 69, 96, 1111]


# print(sum(
#     map(
#         lambda x: abs(x)**2,
#         filter(
#             lambda x: x if -99<=x<=99 and abs(x)%9==0 else 0,
#             numbers
#             )
#             )
#             )
#             )

# print('\n'*5)

# names = ['ульяна', 'арина', 'Дмитрий', 'Сергей', 'Яна', 'мила', 'Ольга', 'софья', 'семён', 'Никита', 'маргарита', 'Василиса', 'Кирилл', 'александр', 'александра', 'Иван', 'андрей', 'Родион', 'максим', 'алиса', 'Артём', 'софия', 'владимир', 'дамир', 'Валерий', 'степан', 'Алексей', 'Марк', 'олег', 'ирина', 'Милана', 'мия', 'денис', 'Фёдор', 'Елизавета', 'айлин', 'Варвара', 'валерия', 'Алёна', 'Николь', 'юлия', 'Ксения', 'пётр', 'георгий', 'Мария', 'глеб', 'илья', 'Захар', 'Дарья', 'Евгения', 'матвей', 'Серафим', 'екатерина', 'Тимофей', 'виктор', 'Егор', 'Ника', 'анна', 'даниил', 'тихон', 'вера', 'кира', 'Эмилия', 'Виктория', 'Игорь', 'полина', 'алина', 'Давид', 'анастасия', 'Вероника', 'ярослав', 'Руслан', 'татьяна', 'Демид', 'амелия', 'Элина', 'Арсен', 'евгений', 'мадина', 'дарина', 'Савелий', 'Платон', 'Аделина', 'диана', 'Айша', 'павел', 'Стефания', 'Тимур', 'Ева', 'Елисей', 'Артемий', 'григорий', 'Мирон', 'Мирослава', 'Мира', 'Марат', 'Лилия', 'роман', 'владислав', 'Леонид']


# print(*sorted(
#              filter(
#                      lambda x: x if x[0] in ('А','М') and len(x)>4 else 0,
#                      map(
#                          lambda x: x.capitalize(),
#                          names
#                         )
#                    )
#             )

#        )

# a = lambda x: 10

# print(type(a))

# a = [1,2]
# b = [3,4]

# i = 2

# if i in (a,b):
#     print('YES')
# else:
#     print('NO')    


# a = dict((('a',1),('b',2)))

# print(a)

# from string import ascii_letters, ascii_uppercase, ascii_lowercase, digits

# error_dict:dict = dict(((ascii_letters,'буквы'),
#                             (ascii_uppercase,'заглавной буквы'),
#                             (ascii_lowercase,'строчной буквы'),
#                             (digits,'цифры')))

# password = 'stepikstepik2'

# check_fun = lambda x,key: set(x).isdisjoint(key)

# #set(password).isdisjoint(set_latin_letters)



# for k in error_dict:
#     print(check_fun(password,k))



# import string

# def verification(login   :str,
#                  password:str,
#                  success:callable,
#                  failure:callable
#                  )->list:
#     flag = False

#     if any(i.isalpha() for i in password if i.lower() in string.ascii_lowercase):
#         if any(i.isupper() for i in password if i in string.ascii_uppercase):
#                 if any(i.lower() for i in password if i in string.ascii_lowercase):
#                         if any(i.isdigit() for i in password):
#                             flag = True
#                         else:
#                             failure(login,'в пароле нет ни одной цифры') 
#                 else:
#                     failure(login,'в пароле нет ни одной строчной буквы')
#         else:
#             failure(login,'в пароле нет ни одной заглавной буквы')
#     else:
#         failure(login,'в пароле нет ни одной буквы')      

#     if flag:
#         success(login)    


seq: list = ['a', 2, 'b', 3, ['1a', '2a', '3a', '4a'], '5A', True, 8.763, ('python', 'c++')]



# def rec_seq(sequens:list, elem:str = None)->list:

#     result_list = list()

#     if elem is not None:
#         result_list.append(elem)


#     for sq in sequens:
#         if len(sq)==1:
#             rec_seq(sequens,sq)
#         else:
#             for sq2 in sq:
#                 rec_seq(sq,sq2)
#     return result_list

# print(rec_seq(seq))                


# a = {'sep' : ',f ', 'end' : ' Finish'}

# print(**a)


# How to merge two dictionaries
# in Python 3.5+

x = 1#{'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}

# c = {'f': 3, 'i': 4}

# zrr = {**x, **y,**c}

# print(**zrr) 
# {'c': 4, 'a': 1, 'b': 3}

#re-assigning the function print
def f():
   kek = 0
   def g():
     nonlocal kek
     kek = 1
     print(kek)
   g()
   
f

