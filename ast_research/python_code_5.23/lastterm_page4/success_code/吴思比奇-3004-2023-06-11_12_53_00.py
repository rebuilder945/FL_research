a=eval(input())
b=[]
for x in a:
    if x>1:
     for i in range(2,x):
        if x%i==0 :
            break
     else:
        b.append(x)
print(b)

