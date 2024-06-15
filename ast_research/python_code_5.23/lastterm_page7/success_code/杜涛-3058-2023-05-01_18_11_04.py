a=''
counts={}
while a!="q":
    a=input() 
    counts[a]=counts.get(a,0)+1
list=list(counts.items())
list.sort(key=lambda x:x[1],reverse=True)
print(list[0][0],list[0][1])
