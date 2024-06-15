a = eval(input())
b = [0]
x = a.count(0)
while 0 in a:
    a.remove(0)
for i in range(x):
    a=a+b
print(a)
