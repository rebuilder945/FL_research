wenzi=input()
dic={}
lst1=[]
lst2=[]
while wenzi!="ok":
    a=eval(wenzi[-2:])
    b=wenzi[0:-3]
    dic[b]=a
    
    lst1.append(b)
    lst2.append(a)
    wenzi=input()
lst1.sort(reverse=True)
lst2.sort(reverse=True)
print(lst1)
print(lst2)
if 'India'in lst1:
    print("yes")
else:
    print("no")
print(sum(lst2))
