n=eval(input())
for i in (100,n):
    b=i//100
    b1=i%(b*100)
    s=b1//10
    s1=b1-(s*10)
    if i==b**3+s**3+s1**3:
        print(i)
    else:
        print("none")
