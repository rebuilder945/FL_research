a = str(input("")).split(",")
b = eval(input())
c = list([a[i],b[i]] for i in range(len(a)))
print(c)
