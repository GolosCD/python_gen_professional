st = 3
end = 5
string = 'beegeek'

otr = string[st:end]

len_ont = len(otr)

string1 = string[:st]+('.'*len_ont)+string[5:]



print(string1,len(string1))
print('')
print(string,len(string))