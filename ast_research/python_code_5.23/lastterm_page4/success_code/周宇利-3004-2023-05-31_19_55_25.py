a=eval(input())
b=[]
for i in a:
    for x in range(2,i//2):
        if i%x==0:
            break
        elif x==i//2-1:
            b.append(i)
        else:
            continue
print(b)
