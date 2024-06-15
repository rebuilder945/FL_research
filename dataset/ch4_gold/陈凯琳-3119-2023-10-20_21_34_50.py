lit=eval(input())
lit.reverse()
lit1=[]
for x in lit:
    if x not in lit1:
        lit1.append(x)
lit1.reverse()
print(lit1)



