s=input().split( )
cishu=[]
for i in s:
    cishu.append(s.count(i))
    maxi=max(cishu)
a=[]
for i in s:
    if s.count(i)==maxi:
        if i not in a:
            a.append(i)
a.sort()
for i in a:
    print(i,maxi)
