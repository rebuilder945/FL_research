a=eval(input())
b=[]
for x in a:
    i>=2
    for i in range(2,x):
        if  x%i==0:
            break
    else: 
        b.append(x)   
print(b)
#因为(2,2)矛盾故x=2时跳过2级for
#因为x%i==0是检测合数才跳出，故为质数是会多次检测，如5%2，5%3，5%4


