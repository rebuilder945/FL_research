wenzi=input()
dic={}
while wenzi!="ok":
    a=eval(wenzi[-2:])
    b=wenzi[0:-3]
    dic[b]=a
    wenzi=input()
lst1=list(dic.keys())
lst2=list(dic.values())
print(lst1)
print(lst2)
if "india"in lst1:
    print("yes")
else:
    print("no")
print(sum(lst2))
