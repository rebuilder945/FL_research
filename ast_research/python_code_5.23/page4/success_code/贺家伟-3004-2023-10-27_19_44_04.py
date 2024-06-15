num=eval(input())
a=[]
for x in num:
    if x>=2:
        for i in range(2,int(x**0.5)+1):
            if x%i!=0:
                a.append(x)
b=[n for n in num if n not in a]
print(b)
