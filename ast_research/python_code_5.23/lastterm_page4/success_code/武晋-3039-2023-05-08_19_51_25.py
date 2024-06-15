lst=eval(input())
a=lst.sorted()
min=a[0]
max=a[-1]
def b(n):
    for i in lst:
        if i==min or i==max:
            del i
        else:
            pass
    return b(n)
print(b)
