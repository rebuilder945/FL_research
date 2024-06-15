n1=input().split(",")
n11=n1.copy()
n2,n3=eval(input())
if n2<len(n1):
    for x in range(n3):
        n11.append(n1[n2])
    print(n11)
else:
    print("error")



