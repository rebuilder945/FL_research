string=input()
numlist=[]
num=''
for x in string:
    if x.isdigit():
        num+=x
    else:
        if num!='':
            numlist.append(num)
        num=''
if numlist==[]:
    print('No digits')
else:
    numlist.sort(key=len)
    print(numlist[-1])
