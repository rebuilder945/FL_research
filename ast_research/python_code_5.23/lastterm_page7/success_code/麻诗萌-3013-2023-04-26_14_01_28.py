n0=input()or'ok'
dic={}
while (n0!='ok'):
    country,data=n0.split()
    dic[country]=eval(data)
    n0=input()or'ok'
lst1=list(dic.keys())
lst1.sort()
lst2=list(dic.values())
lst2.sort()
print(lst1)
print(lst2)
if "India"in dic:
    print("yes")
else:
    print("no")
print(sum(lst2))


