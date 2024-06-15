n = int(input())
i=0
for x in list(range(100,n+1)):
    if int(str(x)[0])**3+int(str(x)[1])**3+int(str(x)[2])**3 == x:
        print(x)
        i=1
if i == 0:
    print("none")

