num=input()
lst=[]
for i in range(len(num)):
    lst.append(int((num)))
    lst[i]=(lst[i]+5)%10
lst[0],lst[-1]=lst[-1],lst[0]
lst[1],lst[-2]=lst[-2],lst[1]
print(lst)
