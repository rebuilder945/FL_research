ls=eval(input())
ls.sort(reverse=True)
for x in ls:
    if ls!=0:
        print(x,end='')
    elif ls[1]==ls[-1]:
        print(0)
