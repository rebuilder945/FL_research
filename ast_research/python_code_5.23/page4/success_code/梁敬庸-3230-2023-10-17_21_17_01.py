a=eval(input())
a.sort(reverse=True)
b=str()
if max(a)>0:
    for x in range(len(a)):
        print(a[x],end='')
else:
    print("0")
