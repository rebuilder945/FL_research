
a=eval(input())
if a==[0,0,0]:
    print(0)
else:
    a.sort(reverse=True)
    for i in range(len(a)):
        print(a[i],end="")
