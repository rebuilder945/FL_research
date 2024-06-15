h = eval(input())
n = eval(input())
sum1 = [h]
n =n-1
while n>0:
    h = h/2
    sum1.append(h)
    n = n-1
    a = sum(sum1)*2-10
print("%.2f"%a)

    
