lst=eval(input())
primenumber=[]
for x in lst:
    for i in range(2,x):
        if x%i==0:
            break
    else:
        if x not in primenumber:
                primenumber.append(x)
if 0 in primenumber:
    primenumber.remove(0)
if 1 in primenumber:
    primenumber.remove(1)
print(primenumber)




