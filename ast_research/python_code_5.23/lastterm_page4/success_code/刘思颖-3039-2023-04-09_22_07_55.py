a = eval(input())
maxvalue = max(a)
minvalue = min(a)
while(maxvalue in a):
    a.remove(maxvalue)
while(minvalue in a):
    a.remove(minvalue)
print(a)

    
