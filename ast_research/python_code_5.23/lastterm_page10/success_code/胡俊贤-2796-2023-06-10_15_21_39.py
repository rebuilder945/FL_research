s=str(input())
temp=[]
long=[]
for i in s:
    if i.isdigit():
        temp.append(i)
    else:
        if len(temp)>=len(long):
            long=temp.copy()
        temp.clear()
print(''.join(long))
        

            

