s1=input()
s2=input()
a1={s1+s2}
s3={"yellow","red","blue"}
purple={"red","blue"}
orange={"red","yellow"}
green={"blue","yellow"}
if s1==s2 or s1 not in s3 or s2 not in s3:
    print("error")
else:
    if a1==purple:
        print('purple')
    elif a1==orange:
        print("orange")
    elif a1==(green):
        print("green")
