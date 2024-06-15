a=eval(input())
a.sort(reverse=True)
s=''
for x in a:
    s+=str(x)
print(int(s))
