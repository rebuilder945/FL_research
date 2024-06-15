dummy=input()
counts={}
while dummy!='q':
    counts[dummy]=counts.get(dummy,0)+1
    dummy=input()
lst=list(counts.items())
lst.sort(key=lambda x:x[1],reverse=True)
print(lst[0][0],lst[0][1])
