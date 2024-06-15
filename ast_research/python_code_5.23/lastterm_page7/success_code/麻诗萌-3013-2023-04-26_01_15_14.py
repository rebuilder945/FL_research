n0=input()or'ok'
dic={}
while (n0!='ok'):
    n=n0.split()
    dic[n[0]]=int(n[1])
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


