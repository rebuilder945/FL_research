n1=eval(input())
n2=[x for x in range(1,n1+1)]
n3=n2[0]
del n2[0]
n2.append(n3)
print(n2)
