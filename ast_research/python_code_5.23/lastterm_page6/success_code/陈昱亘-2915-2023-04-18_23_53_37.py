n=eval(input())
lst=[]
for i in range(n):
    a=(i+1)//100
    b=((i+1)//10)%10
    c=(i+1)%10
    if a**3+b**3+c**3==(i+1) and 0<a<10:
        lst.append((i+1))
        print((i+1))
if lst==[]:
    print('none')
