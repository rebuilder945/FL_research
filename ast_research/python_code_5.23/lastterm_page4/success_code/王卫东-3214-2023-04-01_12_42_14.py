a = eval(input())
s = a.count(0)
for x in a:
    if x == 0:
        a.remove(x)
b = [0]*s
a=a+b
print(a)        
