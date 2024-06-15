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
print(''.join(long))
        

            

