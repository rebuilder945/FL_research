a = eval(input())
b = max(a)
c = min(a)
for i in a:
    if i>=b:
        a.remove(i)
for x in a:
    if x <=c:
        a.remove(x) 
print(a)   
        

