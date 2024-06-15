a=input()
b=0
for i in range(100,1+eval(a)):
    A,B,C=eval(a[0]),eval(a[1]),eval(a[2])
    if (A**3+B**3+C**3)==eval(i):
        print(i)
        b+=1
if b==0:
    print("none")
    
