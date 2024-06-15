a = eval(input())
s = a.count(0)
while a.count(0) >=1:
    a.remove(0)
b = [0]*s
a=a+b
print(a)        
