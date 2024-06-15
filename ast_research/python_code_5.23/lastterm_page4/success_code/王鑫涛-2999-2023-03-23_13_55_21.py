a=input().split(' ')
b=input().split(' ')
q=int(max(b))
w=int(min(b))
e=a.pop(q)
a.insert(w,e)

r=a.pop(w+1)
a.insert(q,r)
print(a)

