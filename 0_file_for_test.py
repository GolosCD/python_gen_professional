import re

test_text = 'Select * from khd_pub.RUFRDM_SBJ_FCT' #Просто тект

test_text_new = 'khd_pub.RUFRDM_SBJ_FCT Select * from ' #Искомое в начел

test_text_full = 'khd_pub.RUFRDM_SBJ_FCT' #Только искомое

re_mask = 'fct\Z'

re_mask = '\w{1,}\_\w{1,}\.\w+'

my_search = re.search(re_mask,test_text)

my_match = re.match(re_mask,test_text_new)

my_match_full = re.fullmatch(re_mask,test_text_full)


print(type(my_search))

print(my_match)

print(my_match_full)


from re import fullmatch

match1 = fullmatch(r'(-)?(\d+)', '2077')
match2 = fullmatch(r'(-)?(\d+)', '-1337')

print(match1.group(1))
print(match1.group(2))
print(match2.group(1, 2))
