s1=eval(input())
s2=eval(input())
if s1=="red" and s2=="blue":
    print("purple")
elif s1=="blue" and s2=="red":
    print("purple")
elif s1=="red" and s2=="yellow":
    print("orange")
elif s1=="yellow" and s2=="red":
    print("orange")
elif s1=="blue" and s2=="yellow":
    print("green")
elif s1=="yellow" and s2=="blue":
    print("green")
else:
    print("error")
