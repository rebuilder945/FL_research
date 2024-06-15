a=eval(input())
b=int(max(a))
c=int(min(a))
lit=[b,c]
lit1=[]
for i in a:
    if i not in lit:
        lit1.append(i)
print(lit1)

