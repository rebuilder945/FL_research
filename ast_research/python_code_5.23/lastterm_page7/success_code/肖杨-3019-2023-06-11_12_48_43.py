name,english,python,math=input().split()
a=list(map(int,[english,python,math]))
a.sort(reverse=True)
b=[]
for i in a:
    b.append('%.2f'%(i))
print(name," ".join(map(str,b)),'%.2f'%(sum(a)/len(a)))

