ll=eval(input())
ii=[]
for i in ll[::-1]:
    if i not in ii:
        ii.append(i)
ii.reverse()

