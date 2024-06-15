a=eval(input())
list1=list(range(1,a+1))
ini=0
n=0
for x in list1:
    if ini==0:
        n=x
        list1[ini]=list1[ini+1]
        ini+=1
    elif 0<ini<len(list1)-1:
        list1[ini]=list1[ini+1]
        ini+=1
    elif ini==len(list1)-1:
        break
list1[ini]=n
print(list1)
