a = tuple((input().split(",")))
c = list(a)
b = eval(input())
for i in range(len(a)):
    d = [[a[i],b[i]]]

    print(d,end=",")
