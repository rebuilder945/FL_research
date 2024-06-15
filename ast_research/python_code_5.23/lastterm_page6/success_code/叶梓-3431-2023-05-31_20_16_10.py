n=eval(input())
if n==0:
    print("green")
elif n in [1,3,5,7,9,12,14,16,18,19,21,23,25,27,29,30,32,34,36]:
    print("red")
elif n in [2,4,6,8,10,11,13,15,17,20,22,24,26,28,31,33,35]:
    print("black")
else:
    print("error")
