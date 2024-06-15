def P(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False               
    return True
num=eval(input())
i=2
t=1
if num<=1 or int(num)!=num:
    print("illegal input")
else:
    while t<num:
        if str(i)==str(i)[::-1] and P(i):
            print(i,end=' ')
        t+=1
        i+=1
