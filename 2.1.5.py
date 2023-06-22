def convert (n:str):
    len_low = len(list(filter(lambda x: x.islower() and x.isalpha,list(n))))
    len_upp = len(list(filter(lambda x: x.isupper() and x.isalpha,list(n))))
    if len_low>=len_upp:
        return n.lower()
    else:
        return n.upper()
        
print(convert('pi31415!'))      