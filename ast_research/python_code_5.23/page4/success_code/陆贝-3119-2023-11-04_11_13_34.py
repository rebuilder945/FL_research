a=eval(input())
ii=[]
for i in a[::-1]:
    if i not in ii:
        ii.append(i)
ii.reverse()
print(ii)
