clo1 = input()
clo2 = input()
s = {clo1,clo2}
s1 = {"red","blue"}
s2 = {"red","yellow"}
s3 = {"blue","yellow"}
if s in s1:
    print("purple")
elif s in s2:
    print("orange")
elif s in s2:
    print("green")
else:
    print("error")
