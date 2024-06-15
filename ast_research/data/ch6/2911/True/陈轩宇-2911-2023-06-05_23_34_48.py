n = eval(input())
sum1 = 0
new = [sum1]
while n>0:
    sum1=(n%10+5)%10
    n = n//10
    new.append(sum1)
del new[0]
new = list(map(str,new))
print("".join(new))
