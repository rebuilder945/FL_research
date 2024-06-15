num=eval(input())
c=[]
if num<=100:
    print("none")
else:
    for i in range(100,num+1):
        i=str(i)
        if int(i[0])**3+int(i[1])**3+int(i[2])**3==int(i):
            print(i)
            c.append(i)
    if len(c)==0:
        print("none")
    
