n=input()
number=[x for x in range(0,37)]
if n in range(1,11):
    if n in number[1:11:2]:
        print("red")
    if n in number[2:11:2]:
        print("black")
if n in range(11,19):
    if n in number[11:19:2]:
        print("black")
    if n in number[12:19:2]:
        print("red")
if n in range(19,29):
    if n in number[19:29:2]:
        print("red")
    if n in number[20:29:2]:
        print("black")
if n in range(29,37):
    if n in number[29:37:2]:
        print("black")
    if n in number[30:37:2]:
        print("red")
elif n==0:
    print("green")
else:
    print("error")

