dic={}
m=input()
while m !='ok':
    m,n=map(str,m.split())
    dic[m]=int(n)
    m=input()
lst1=[]
lst2=[]
for i in dic.keys():
    lst1.append(i)
for i in dic.values():
    lst2.append(i)
lst1.sort()
lst2.sort()
print(lst1)
print(lst2)
if 'India' in lst1:
    print("yes")
if 'India' not in lst1:
    print("no")
print(sum(lst2))

    



