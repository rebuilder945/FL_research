a=eval(input())
a.sort(reverse=True)
b=""
for i in range(len(a)):
    c=str(a[i])
    b=b+c
if b.count("0")==len(b):
    print(0)
else:
    print(b)






