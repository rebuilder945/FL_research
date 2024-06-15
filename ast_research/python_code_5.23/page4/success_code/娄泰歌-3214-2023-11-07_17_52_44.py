ls=eval(input())
lt1=[]
lt2=[]
for i in range(len(ls)):
    if ls[i]==0:
        lt1.append(0)
    else:
        lt2.append(ls[i])
print(lt2+lt1)
