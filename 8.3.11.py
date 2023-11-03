def to_binary(number:int)->int:
    
    binary_result:str = ''
    
    def number_drop(dig:int,res:str)->str:
        if dig==0:
            res=res+'1'
        elif dig%2==1:
            res=res+'1'
        else:
            return number_drop(number//2,res)
        return res    
    
    #number_drop(number,binary_result)
            
    return number_drop(number,binary_result)        

print(to_binary(15))



















a = 15 #1111
print('\n'*3)
print('=====================')
print(a%2,a//2)
print(7%2,7//2)
print(3%2,3//2)
print(1%2,1//2)
print('=====================')