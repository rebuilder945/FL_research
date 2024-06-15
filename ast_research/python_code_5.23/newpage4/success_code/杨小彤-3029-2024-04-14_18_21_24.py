a = str(input("")).split(",")
b = eval(input())
for i in range(len(a)):
    print([[a[i],b[i]]],end = ",")

