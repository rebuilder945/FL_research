n=eval(input())
n1=n.copy()
while 0 in n:
    n.remove(0)
    n1.remove(0)
    n1.append(0)
print(n1)
    








