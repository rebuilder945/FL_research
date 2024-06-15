n = eval(input())
a = [x for x in range (1,n+1)]
for i in range(1):
    num = a.pop(0)
    a.append(num)
print(a)
