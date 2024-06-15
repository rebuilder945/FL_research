n = eval(input())
flag = 0
sum = 0
for i in range(100,n+1):
    sum = int(str(i)[0])**3+int(str(i)[1])**3+int(str(i)[2])**3
    if sum == i:
        print(i)
        flag = 1
if flag == 0:
    print("none")
