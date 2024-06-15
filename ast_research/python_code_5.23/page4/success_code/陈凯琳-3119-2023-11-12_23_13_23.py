a=eval(input())
a.reverse()
lit=[]
for i in a:
    if i not in lit:
        lit.append(i)
lit.reverse()
print(lit)

