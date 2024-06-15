def sxhs(x):
    b=str(x)
    if x==int(b[0])**3+int(b[1])**3+int(b[2])**3:
        return True
    return False
a=eval(input())
for x in range(100,a+1):
    if sxhs(x):
        print(x)
        break
else:
    print("none")
