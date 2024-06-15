a=eval(input())
a.sort(reverse=True)
b=''
for i in a:
    if max(a)!=0:
        b+=str(i)
    else:
        b=0  
print(b)




