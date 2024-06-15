a = eval(input())
for i in range (a):
    k=a.count(i)
    for i in range(k):
        if k >1:
            a.pop(i)
        else:
            print(a)
