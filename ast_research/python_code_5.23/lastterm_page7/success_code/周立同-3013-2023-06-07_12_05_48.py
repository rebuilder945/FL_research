a=input()
lst=a.split()
dic={}
while a!="ok":
    dic[lst[0]]=eval(lst[1])
    a=input()
    lst=a.split()
lst1=list(dic.keys())
lst1.sort()
lst2=list(map(int,list(dic.values())))
lst2.sort()
print(lst1)
print(lst2)
if "India" in lst1:
    print("yes")
else:
    print("no")
print(sum(lst2))
