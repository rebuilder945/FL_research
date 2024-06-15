a=eval(input())
q={1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36}
w={2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35}
e={0}
if a in q:
    print("red")
elif a in w:
    print("black")
elif a in e:
    print("green")
else:
    print("error")

