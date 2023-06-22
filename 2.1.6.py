def filter_anagrams(wordr:str,*argsr):
    w = sorted(wordr)
    for i in argsr:
        return list(filter(lambda x: w==sorted(x),i))



word = 'abba'
anagrams = ['aaab', 'dbcd', 'bdaa', 'badb']
    
print(filter_anagrams(word, anagrams))    


