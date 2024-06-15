a=int(input())
c=False
for x in range(2,a+1):
    b=0
    for i in str(x):
        b=int(i)**3+b
    if b==int(x):
        print(int(x))
        c=True
if not c:
    print('none') 
