n1=eval(input())
n2=[x+1 for x in range(n1)]
n22=n2.copy()
n22.pop(0)
n22.append(n2[0])
print(n22)
