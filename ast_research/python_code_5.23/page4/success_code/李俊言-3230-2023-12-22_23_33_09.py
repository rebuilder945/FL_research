ls=eval(input())
s=''
for x in range(len(ls)):
    a=max(ls)
    s+=str(a)
    ls.remove(a)
print(int(s))














