a=input().split(' ')
b=input().split(' ')
q=int(max(b))
w=int(min(b))
e=a.pop(q)
a.insert(q,0)
r=a.pop(w)
a.insert(w,1)
a[q]=r
a[w]=e
print(a)
