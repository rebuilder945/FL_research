s=input()
l=[0 for i in range(len(s)+1)]
for j in range(len(s)):
    if s[j].isdigit():
        l[j]=l[j-1]+1
for t in range(len(l)-1,-1,-1):
    if l[t]==max(l):
        d=t
        break
if max(l)!=0:
    print(s[d-max(l)+1:d+1])
else:
    print('No digits')
