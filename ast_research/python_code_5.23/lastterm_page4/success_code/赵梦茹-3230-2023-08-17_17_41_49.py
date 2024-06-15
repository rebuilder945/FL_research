a=eval(input())
a.sort(reverse=True)
if a[0]==0:
    print(0)
else:
    for i in a:   
        print(i,end='')

