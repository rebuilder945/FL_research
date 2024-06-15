a=eval(input())
ls=[]
for i in range(100,a+1):
    if i==int(str(i)[0])**3+int(str(i)[1]):
        ls.append(i)
if len(ls)==0:
    print("none")
else:
    for x in ls:
        print(x)
