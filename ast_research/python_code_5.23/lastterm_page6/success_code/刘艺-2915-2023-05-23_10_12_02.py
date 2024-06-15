a = eval(input())
i = 0
for x in range(100,a+1):
    if int(str(x)[0])**3 + int(str(x)[1])**3 + int(str(x)[2])**3 == x:
        print(x)
        i += 1
    else:
        pass
if i == 0:
    print("error")

