def search(x):
    a=list(str(x))
    for d in range(len(a)):
        a[d]=int(a[d])
    if a[0]**3+a[1]**3+a[2]**3==x:
        print(x)
t=eval(input())
for y in range(100,t+1):
    search(y)
