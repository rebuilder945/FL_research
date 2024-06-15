ls=eval(input())
ls.sort(reverse=True)
num=""
for i in range(len(ls)):
    a=max(ls)
    b=str(a)
    num += str(b)
    ls.remove(a)
print(num)
