x=input()
length=len(x)
q=0
j=0
for n in x:
    if ord('a')<=int(ord(n))<=ord('z') or ord('A')<=int(ord(n))<=ord('Z'):
        q=q+1
    elif type(eval(n))==int:
        j=j+1
p=x.count(' ')
k=length-q-p-j
print(q,p,j,k)

