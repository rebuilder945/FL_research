n=input()
lst=[]
for i in n:
    m=(int(i)+5)%10
    lst.append(str(m))
lst[0],lst[-1],lst[1],lst[-2]=lst[-1],lst[0],lst[-2],lst[1]
print(lst)   
print("".join(lst))
