s=list(input())
ss=[]
for i in s:
    if s.count(i)==1:
        ss.append(i)
if len(ss)==0:
    print("None")
else:    
    print(str(ss[0]))

