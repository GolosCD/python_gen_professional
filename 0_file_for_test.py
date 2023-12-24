numbers = [1, 2, 3, 4, 7, 8, 10]

for index , val in enumerate(numbers,start=0):
    curent_val = val
    curent_index = index
    try:
        next_val = numbers[curent_index+1]
        last_val = numbers[curent_index-1]
    except:
        next_val = curent_val
        last_val = curent_val
        
    # print('=================================')    
    # print(f'curent_val:= {curent_val}')
    # print(f'curent_index:= {curent_index}')
    # print(f'next_val:= {next_val}')
    # print(f'last_val:= {last_val}')
    # print('=================================')    
        
    if next_val-curent_val==1:
        
        print(f'({curent_val}:{next_val})')
    elif next_val-curent_val!=1 and curent_val-last_val==1:
        continue
    else:
        print(f'({curent_val}:{curent_val})')
        
    # print(f'{index} : {val}')
    
    
print(len(numbers),numbers.index(10))    