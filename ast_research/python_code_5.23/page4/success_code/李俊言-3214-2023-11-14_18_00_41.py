def sxhs(x):
    b=str(x)
    if x==int(b[0])**3+int(b[1])**3+int(b[2])**3:
        return True
    return False
a=eval(input())
b=[]
for x in range(100,a+1):
    while sxhs(x):
        print(x)
        b.append(x)
        break 
if b==[]:
    print("none")

