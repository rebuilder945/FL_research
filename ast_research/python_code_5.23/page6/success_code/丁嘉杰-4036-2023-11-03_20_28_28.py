s1={"ji":"red","ou":"black"}
s2={"ji":"black","ou":"red"}
n=int(input())
if n<0 or n>36:
    print("error")
elif n==0:
    print("green")
elif 0<n<11 or 18<n<29:
    if n%2==0:
        print(s1["ou"])
    else:
        print(s1["ji"])
else:
    if n%2==0:
        print(s2["ou"])
    else:
        print(s2["ji"])
