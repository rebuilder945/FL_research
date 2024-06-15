a=input()
lst=[]
for i in range(int(a)+1):
    if int(a[0])**2 + int(a[1])**2 + int(a[2])**2 == int(a):
        lst.append(i)
if lst:
    for x in lst:
        print(x)
else:
    print("none")
