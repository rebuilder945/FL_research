a=input().split() or "ok"
dic={}
print(a)
while a!="ok":
    dic[a[0]]=a[-1]
    a=input().split() or "ok"
lst1=list(dic.keys())
lst=list(dic.values())
lst1.pop()
lst.pop()
lst2=list(map(eval,lst))
lst1.sort(reverse=False)
lst2.sort(reverse=False)

print(lst1)
print(lst2)
if 'India' in lst1:
    print('yes')
else:
    print('no') 
print(sum(lst2))
