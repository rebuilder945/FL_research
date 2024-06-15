s=input()
slst=list(s)
print(s)
up = [chr(i) for i in range(ord('A'), ord('Z')+1)]
low = [chr(i) for i in range(ord('a'), ord('z')+1)]
for i in slst:
    for j in range(26):
        if i==up[j]:
            a=s.find(i)
            slst[a]=up[26-j-1]
        elif i==low[j]:
            a=s.find(i)
            slst[a]=low[26-j-1]        
print("".join(slst))
