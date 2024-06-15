from audioop import reverse


a=eval(input())
a.sort(reverse=True)
m=''
for i in a:
    m=m+str(i)
print(int(m))



