a=eval(input())
if a.count(0)==0:
    print(a)
else:
    for i in range(a.count(0)):
        a.remove(0)
        a.append(0)
    print(a)
    
