num=input()
lst=[]
for x in num:
    y=(int(x)+5)%10
    lst.append(y)
for x in range(len(lst)//2):
    lst[x],lst[-1-x]=lst[-1-x],lst[x]
lst=list(map(str,lst))
a="".join(lst)
print(a)
