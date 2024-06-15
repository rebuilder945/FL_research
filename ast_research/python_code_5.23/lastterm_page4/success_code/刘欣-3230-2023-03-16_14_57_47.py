ls=eval(input())
ls.sort(reverse=True)
num=""
for i in range(len(ls)):
    a=max(ls)
    if a!=0:
        b=str(a)
        num += str(b)
        ls.remove(a)
        print(num)
    else:
        a==0
        print("0")
