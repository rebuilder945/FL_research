ls=eval(input())
ls.sort(reverse=True)
for x in ls:
    print(x,end='')
if ls==0:
    print(0)
