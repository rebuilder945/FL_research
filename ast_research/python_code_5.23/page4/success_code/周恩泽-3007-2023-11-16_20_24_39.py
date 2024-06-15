n1=eval(input())
n2,n3=eval(input())

if n2>n3 or n2>len(n1 ) or n3>len(n1):
    print("error")

else:     
    for x in range(n2,n3):
        n1.pop(x)
    print(n1)

