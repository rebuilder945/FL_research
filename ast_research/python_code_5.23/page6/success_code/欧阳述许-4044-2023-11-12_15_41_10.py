n=eval(input())
count=0
for i in range(104,n+1):
    a=eval(str(i)[0])
    b=eval(str(i)[1])
    c=eval(str(i)[2])
    if (a**3+b**3+c**3)==i:
        print(i)
        count+=1
    if count==0:
        print("none")

