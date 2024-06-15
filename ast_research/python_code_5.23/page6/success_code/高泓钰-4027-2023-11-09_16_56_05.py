a=0
n=0
eva=0
b=input()
while b!='#':
    b=input()
    if b!='#':
        a=eval(b)
    n+=1
    eva+=a
print(n,eva)

