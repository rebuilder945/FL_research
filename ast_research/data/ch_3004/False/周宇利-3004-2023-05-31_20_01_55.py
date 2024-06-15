a=eval(input())
b=[]
for i in a:
    for j in range(2,i//2):
        if i%j==0:
            break
        else:
            b.append(i)
print(b)
