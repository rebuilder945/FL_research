lst=eval(input())
new=[]
for x in lst:
    if x >2:
        for i in range(2,x):
            if x%i==0:
                flag=False
                break
            else:
                new.append(x)
print(new)
