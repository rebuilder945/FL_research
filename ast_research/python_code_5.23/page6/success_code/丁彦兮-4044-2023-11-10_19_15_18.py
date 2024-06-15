a=eval(input())
b=[]
for x in range(100,a+1):
    x=str(x)
    if int(x[0])**3+int(x[1])**3+int(x[2])**3==int(x):
       print(x)
       b.append(x)
if b==[]:
    print("none")
    


