a=eval(input())
su=[]
for i in a:
    if i >=2:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            su.append(i)
print (su)
