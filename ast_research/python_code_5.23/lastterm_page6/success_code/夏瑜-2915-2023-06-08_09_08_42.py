a=int(input())
if a<=100 or a>=1000:
    print("None")
elif 101<=a<1000:
    for i in range(101,a):
        if i==int(str(i)[0])**3+int(str(i)[1])**3+int(str(i)[2])**3 :
            print(i)
else:
    print("None")

