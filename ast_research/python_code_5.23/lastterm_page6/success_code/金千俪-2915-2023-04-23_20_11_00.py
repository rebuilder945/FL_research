a=input()
lst=[]
for i in range(100,int(a)+1):
    i=str(i)
    if int(i[0])**3 + int(i[1])**3 + int(i[2])**3 == int(i):
        lst.append(i)
if lst:
    for x in lst:
        print(x)
else:
    print("none")
