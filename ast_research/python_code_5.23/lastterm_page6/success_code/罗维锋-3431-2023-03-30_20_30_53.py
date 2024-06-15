n=eval(input())
g="green"
r="red"
b="black"
if n==0:
    print(g)
elif n in range(1,11):
    if n%2==0:
        print(b)
    else:
        print(r)
elif n in range(11,19):
    if n%2==0:
        print(r)
    else:
        print(b)
elif n in range(19,29):
    if n%2==0:
        print(b)
    else:
        print(r)
elif n in range(29,37):
    if n%2==0:
        print(r)
    else:
        print(b)
else:
    print("error")
