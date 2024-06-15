n=input().split() or'ok'
dic={}
while (n!='ok'):
    dic[n[0]]=int(n[1])
    n=input().split()or 'ok'
lst1=dic.keys().sort()
lst2=dic.values().sort()
print(lst1)
print(lst2)
if "India"in dic:
    print("yes")
else:
    print("no")
print(sun(lst2))


