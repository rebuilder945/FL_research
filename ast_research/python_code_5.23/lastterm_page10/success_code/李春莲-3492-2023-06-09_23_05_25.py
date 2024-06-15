s=list(str(input()))
if s==(' '):
    print("None")
l=[]
for i in range(len(s)+1):
    if s.count(s[i])==1:
        l.append(i)
        print(l[0])
