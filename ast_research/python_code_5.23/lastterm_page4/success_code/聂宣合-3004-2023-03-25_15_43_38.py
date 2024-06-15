lst=eval(input())
primenumber=[]
for x in lst:
    for i in range (2,x-1):
        if x%i==0:
            break
        else:
            if x not in primenumber:
                primenumber.append(x)

print(primenumber)




