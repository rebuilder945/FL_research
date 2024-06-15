a=eval(input())
a.sort(reverse=True)
if a[0]>0:
    for t in range(len(a)):
        print(a[t],end='')
else:
    print(0)
