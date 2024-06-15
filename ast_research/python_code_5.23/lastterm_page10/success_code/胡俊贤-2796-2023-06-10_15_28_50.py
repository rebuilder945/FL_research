s=str(input())
temp=[]
long=[]
for i in s:
    if i.isdigit():
        temp.append(i)
        if len(temp)>=len(long):
            long=temp.copy()
    else:
        temp.clear()
if long==[]:
    print('No digits')
else:
    print(''.join(long))
        

            

