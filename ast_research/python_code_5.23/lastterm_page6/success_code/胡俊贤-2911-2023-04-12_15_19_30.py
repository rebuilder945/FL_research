num=input()
lst=list(map(int,num))
for i in range(0,len(lst)):
    lst[i]=str((lst[i]+5)%10)
lst.reverse()
num0="".join(lst)
print(num0)

