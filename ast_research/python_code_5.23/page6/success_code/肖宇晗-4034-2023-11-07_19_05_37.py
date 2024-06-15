clo1 = input()
clo2 = input()
s = {clo1,clo2}
s1 = {"red","blue"}
s2 = {"red","yellow"}
s3 = {"blue","yellow"}
if s == s1:
    print("purple")
elif s == s2:
    print("orange")
elif s == s3:
    print("green")
elif s not in {"red","blue","yellow"}:
    print("error")
else:
    print("error")
