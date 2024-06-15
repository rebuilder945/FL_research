a=eval(input())
x=0
flag=False
for i in range(2,a+1):
    for n in str(i):
        x+=int(n)**3
    if x==i:
        flag=True
        print(i)
if flag==False:
    print("None")
