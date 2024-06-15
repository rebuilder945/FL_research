
a=eval(input())
if x in a not in range(1,10):
    print(0)
else:
    a.sort(reverse=True)
    for i in range(len(a)):
        print(a[i],end="")
