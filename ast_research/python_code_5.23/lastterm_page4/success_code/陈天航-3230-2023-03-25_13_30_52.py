ls=eval(input())
ls.sort(reverse=True)
for x in ls:
    print(x,end='')
    if x==0:
        print(0)
