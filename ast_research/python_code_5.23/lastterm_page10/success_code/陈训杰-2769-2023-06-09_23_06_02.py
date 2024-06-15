s=input()
slst=list(s)
print(s)
s1=""
up = [chr(i) for i in range(ord('A'), ord('Z')+1)]
low = [chr(i) for i in range(ord('a'), ord('z')+1)]
for i in slst:
    if i.islower() or i.isupper():
        for j in range(26):
            if i==up[j]:
                s1+=up[26-j-1]
                break
            elif i==low[j]:
                s1+=low[26-j-1]   
                break       
    else:
        s1+=i
print(s1)
