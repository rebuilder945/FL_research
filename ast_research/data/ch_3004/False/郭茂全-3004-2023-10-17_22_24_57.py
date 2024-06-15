list=eval(input())
a=[]
for x in list:
    if x == 1:
        continue
    else:
        for i in range(2,x):
            if x%i==0:
                break
            else:
                a.append(x)
print(a)
