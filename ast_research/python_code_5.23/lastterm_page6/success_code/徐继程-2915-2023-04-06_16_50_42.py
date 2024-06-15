num=eval(input())
d=0
for i in range(100,num+1):
    i=str(i)
    a=eval(i[0])
    b=eval(i[1])
    c=eval(i[2])
    
    if a**3+b**3+c**3==int(i):
        print(int(i))
        d+=1
if d==0:
    print('none')
