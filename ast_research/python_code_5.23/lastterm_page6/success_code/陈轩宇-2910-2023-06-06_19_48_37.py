h = eval(input())
n = eval(input())
sum1 = h
n = n-1
save = [sum1]
while n>0:
    h= h*(1/2)
    save.append(h)
    n=n-1
    x = sum(save)
    x1 = x*2-sum1
    
print("%.2f"%x1)

    
