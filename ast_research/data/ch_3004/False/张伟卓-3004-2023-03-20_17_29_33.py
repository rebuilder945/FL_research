lt1=eval(input())
lt2=[]
for x in lt1:
    for i in range (2,x):
        if x % i == 0:
            break
else:
    lt2.append(x)
print(lt2)


