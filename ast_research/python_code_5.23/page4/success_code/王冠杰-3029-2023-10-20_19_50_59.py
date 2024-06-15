a=input().split(',')
b=eval(input())
c=list(a)
d=()
e=[]
for i in range(len(c)) :
    d=(c[i],b[i])
    e.append(list(d))
print(e)
