ls=eval(input())
ls.sort(reverse=True)
for x in ls:
    if ls[1]!=ls[-1]:
        print(x,end='')
if ls[1]==ls[-1]:
    print(0)
