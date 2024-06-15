n = eval(input())
a = 1
b = 2
list =[]
for i in range(1,n+1):
        a,b,c = b,b+a,b/a
        list.append(c)
        s = sum(list)
print("%.4f"%s)

