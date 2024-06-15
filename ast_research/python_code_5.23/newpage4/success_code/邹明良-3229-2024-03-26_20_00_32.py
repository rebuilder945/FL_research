# import re
# s = input()
# ls = map(int,re.split(r'[[],]',s))
ls = list(eval(input()))
flag = 0
alone=[]
ls.sort()
len=len(ls)
for i in range(len):
    num=ls.count(ls[i])
    if num==1:
        flag = 1
        alone.append(ls[i])
if flag:
    print(alone)
else:
    print('False')
