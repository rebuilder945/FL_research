def sxh(n):
    if int(str(n)[0])**3+int(str(n)[1])**3+int(str(n)[2])**3==n:
        return True
    else:
        return False
a=eval(input()) 
for x in range(100,a+1):   
    if sxh(x):
        print(x)
else:
    print("none")        
