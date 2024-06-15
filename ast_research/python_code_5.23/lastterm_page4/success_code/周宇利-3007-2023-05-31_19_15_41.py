a=eval(input())
b=[]
n,m=input().split(",")
x=0
if int(n) in range(0,len(a)) and int(m) in range(0,len(a)):
    for i in a:
        if x not in range(int(n),int(m)):
            b.append(i)
            x+=1
            print(b)
else:
    print("error")
