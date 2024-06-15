num=eval(input())
for x in num:
    if x>=2:
        for i in range(2,int(x**0.5)+1):
            if x%i==0:
                num.remove(x)
print(num)
