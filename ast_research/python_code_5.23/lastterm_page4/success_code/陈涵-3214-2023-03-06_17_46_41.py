num=eval(input())
n=num.count(0)
num2=num.copy()
for x in num2:
    if x == 0:
        num.remove(x)
for x in range(n):
    num.append(x*0)
print(num)                     
