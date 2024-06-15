a1=input()
a2=input()
a={a1,a2}
s={"red","yellow","blue"}
s1={"red","yellow"}
s2={"red","blue"}
s3={"yellow","blue"}
if a==s1:
    print("orange")
elif a==s2:
   print("purple")
elif a==s3:
    print("green")
elif a1==a2 or (a1 not in s and a2 not in s):
    print("error")
