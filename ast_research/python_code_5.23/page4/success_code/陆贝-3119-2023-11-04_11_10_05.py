a=eval(input())
ii=[]
for i in a:
    if i not in ii:
        ii.append(ii)
print(ii)
