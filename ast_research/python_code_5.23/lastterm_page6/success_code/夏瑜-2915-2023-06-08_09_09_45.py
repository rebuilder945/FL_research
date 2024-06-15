a=int(input())
if a<=100 :
    print("none")
elif 101<=a:
    for i in range(101,a+1):
        if i==int(str(i)[0])**3+int(str(i)[1])**3+int(str(i)[2])**3 :
            print(i)
else:
    print("none")

