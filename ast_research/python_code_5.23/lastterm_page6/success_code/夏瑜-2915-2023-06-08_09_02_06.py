a=int(input())
if a<=100 or a>=1000:
    print("None")
elif a==int(str(a)[0])**3+int(str(a)[1])**3+int(str(a)[2])**3:
    print(a)
else:
    print("None")

