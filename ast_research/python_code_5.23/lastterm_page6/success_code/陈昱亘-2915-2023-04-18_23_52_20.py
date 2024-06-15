n=eval(input())
lst=[]
for i in range(n):
    a=i//100
    b=(i//10)%10
    c=i%10
    if a**3+b**3+c**3==i and 0<a<10:
        lst.append(i)
        print(i)
if lst==[]:
    print('none')
