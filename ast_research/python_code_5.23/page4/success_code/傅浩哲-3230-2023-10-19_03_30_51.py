a=eval(input())
b=''
for i in a:
    if i==max(a):
        b=b+str(i)
        a.replace(i,0)
print(b)
