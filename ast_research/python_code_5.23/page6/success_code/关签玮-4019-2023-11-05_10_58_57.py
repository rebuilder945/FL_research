a=str(input())
lst=[]
for i in a:
    i=(int(i)+5)%10
    lst.append(i)
for x in range(len(lst)//2):
    lst[x],lst[-x-1]=lst[-x-1],lst[x]
for y in lst:
    print(y,end="")
