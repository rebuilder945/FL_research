v=eval(input())
chars=[chr(x) for x in range(ord('a'),ord('z')+1)]
counts=[0]*26
for x in v:
    for c in x:
        counts[ord(c)-ord('a')]+=1
for c,cnt in zip(chars,counts):
    if cnt > 0:
        print("%s,%d"%(c,cnt))
