a=input().split(' ')
b=input().split(' ')
q=int(max(b))
w=int(min(b))
if not q == w:
    e=a.pop(q)
    a.insert(w,e)
    r=a.pop(w+1)
    a.insert(q,r)
else:
    pass
print(a)

