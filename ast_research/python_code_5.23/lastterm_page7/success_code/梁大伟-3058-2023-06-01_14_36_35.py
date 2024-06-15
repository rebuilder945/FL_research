a=input() or 'q'
d={}
while a!='q':
    d[a]=d.get(a,0)+1
    a=input() or 'q'
lst=[]
for k,v in d.items():
    lst.append([k,v])
lst.sort(key=lambda x:x[1],reverse=True)
print(lst[0][0],lst[0][1])
