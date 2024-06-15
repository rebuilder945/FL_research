a=eval(input())
s=0
for x in range(100,a):
    for i in str(x):
        i=int(i)
        s+=i**3
    if s==x:
        print(x)
else:
    print('none')
