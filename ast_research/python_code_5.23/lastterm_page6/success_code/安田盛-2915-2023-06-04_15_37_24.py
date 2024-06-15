n=eval(input())
a=[]
if n<=100:
    print("none")
elif n>=1000:
    for i in range(100,1000):
        if int(str(i)[0])**3+int(str(i)[1])**3+int(str(i)[2])**3== i:
            a.append(i)
    
else:
    for i in range(100,n+1):
        if int(str(i)[0])**3+int(str(i)[1])**3+int(str(i)[2])**3== i:
            a.append(i)
if a==[]:
    print("none")
else:
    for i in a:
        print(i)



