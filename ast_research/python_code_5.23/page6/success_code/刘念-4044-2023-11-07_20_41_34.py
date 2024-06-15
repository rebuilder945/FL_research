e = eval(input())
f = 0
for i in range(100,e+1):
    a = i%10  
    b = i//10
    c = b%10
    d = c//10
    if a*a*a+c*c*c*+d*d*d ==i:
        f = f+1
        print(i)
if f == 0:
    print('none')
    


