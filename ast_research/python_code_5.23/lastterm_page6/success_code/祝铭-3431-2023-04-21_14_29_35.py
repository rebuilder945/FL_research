p = eval(input())
bl = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
re = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
gr = [0]
if p in bl :
    print("black")
elif p in gr :
    print("green")
elif p in re :
    print("red")
else:
    print("error")
