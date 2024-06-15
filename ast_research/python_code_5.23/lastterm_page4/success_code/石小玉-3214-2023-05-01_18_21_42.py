Li=eval(input())
x=Li.count(0)
p=0
while p < x:
    Li.remove(0)
    
q=0
while q < x:
    Li.append(0)
    
print(Li)


