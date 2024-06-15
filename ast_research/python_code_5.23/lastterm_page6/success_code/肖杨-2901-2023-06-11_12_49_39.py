b=[0]
i=0
while b[-1]!='#':
    a=input()
    b.append(a)
    i+=1
b.remove('#')
print(i-1,sum(map(int,b)))




