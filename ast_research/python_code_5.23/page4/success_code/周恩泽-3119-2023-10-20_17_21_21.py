n1=eval(input())
n2=[]
for x in n1[::-1]:
    if x not in n2:
        n2.append(x)
print(n2[::-1])
