sNature=eval(input())
lst=[]
for i in sNature:
    if i>=2:
        for j in range(2,i,1):
            if i%j==0:
                break;
        else:
            lst.append(i)
print(lst)
