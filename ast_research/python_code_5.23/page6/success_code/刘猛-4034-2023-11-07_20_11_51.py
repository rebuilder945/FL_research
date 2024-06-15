c1 = str(input())
c2 = str(input())
s1 = set()
s1.add(c1)
s1.add(c2)
if s1 == {"red","blue"}:
    print("purple")
elif s1 == {"red","yellow"}:
    print("orange")
elif s1 == {"blue","yellow"}:
    print("green")
else:
    print("error")

