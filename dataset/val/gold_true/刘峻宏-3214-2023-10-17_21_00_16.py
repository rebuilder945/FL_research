from os import remove


a=eval(input())
for i in range(len(a)):
    if 0 in a:
        a.remove(0)
        a.append(0)
    else:
        break
print (a)
    
    
