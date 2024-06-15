n=eval(input())
lst=[]
for i in range(100,n+1):
    if i<1000:
        a=i//100
        b=(i-a*100)//10
        c=i%10
        if a**3+b**3+c**3==i:
            print(i)
            lst.append(i)
if lst==[]:
    print('none')
