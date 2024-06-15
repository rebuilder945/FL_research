a=eval(input())
b=''
a.sort(reverse=True)
for i in a:
    if max(a)!=0:
        b=b+str(i)
    else:
        b='0'
        break
print(b)
