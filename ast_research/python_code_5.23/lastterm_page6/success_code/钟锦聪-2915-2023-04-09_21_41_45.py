n = int(input())
if n <153:
    print("none")
else:
    for i in range(100,n+1):
        if int(str(i)[0])**3+int(str(i)[1])**3+int(str(i)[2])**3 ==i:
            print(i)

     

