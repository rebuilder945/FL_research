s=input()
m1=0
m2=0
m3=0
m4=0
for i in s:
    if "a"<=i<="z" or "A"<=i<="Z":
        m1+=1
    elif 0<=i<=9:
        m2+=1
    elif i==(" "):
        m3+=1
    else:
        m4+=1
print(m1,m2,m3,m4)
