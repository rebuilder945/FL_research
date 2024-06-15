a=eval(input())
if a <=100:
    print("none")
else:
    for i in range(100,a):
        s=str(i)
        if int(s[0])**3+int(s[1])**3+int(s[2])**3==i:
            print("%d\n",i)
        else:
            print("none")
        
    
