n=int(input())
if n<153:
    print("none")
if n>=153:
    for i in range(153,n+1):
        if int(str(i)[0])**3+int(str(i)[1])**3+int(str(i)[2])**3==i:
            print(i)

