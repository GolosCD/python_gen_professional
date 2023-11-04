from collections import Counter

#n = int(input())

st:list = [3,7,8,10,15]#[int(input()) for _ in range(n)]

# with open ('yandex.txt','r') as open_file:
#     a = Counter(open_file.read().split())

st_c:dict = Counter(st)

result:list = list()

if list(st_c.keys())==['0','1']:
    for _ in range(st_c.get('0')):
        print(st_c.get('1'),end=' ')
else:    
    for first_num in st_c:
        tmp_num =0
        for second_num in st_c:
            if first_num!=second_num:
                tmp_num+=abs(int(first_num)-int(second_num))

        result.append(tmp_num)        




print(*result)

# 1 1
# 1 3
# 1 4

# 3 1
# 3 3
# 3 4

# 4 1
# 4 3
# 4 4

#dd={1: [3,4],3:[1,4],4:[1,3]}

# for i in dd:
#     print(dd.get(i)-dd.get(i+1))

#print({3,1}-{1})

# print({1,4}-{1,3})
# print({1,3}-{3,4})

# print(abs(1-1)+abs(3-1)+abs(4-1))
# print(abs(1-3)+abs(3-3)+abs(4-3))
# print(abs(1-4)+abs(3-4)+abs(4-4))

# min_num = min(st)

# st.pop()

# print(st)

#print([abs((sum(st)-min(st))-i*len(st)-1)+abs(min(st)-i)for i in st])