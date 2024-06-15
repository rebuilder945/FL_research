a=eval(input())
b=[]
for x in a:
    b.append(x)
b.sort(reverse=True)
if b[0]==0:
    print(0)
else:
    print("".join(str(x) for x in b))
