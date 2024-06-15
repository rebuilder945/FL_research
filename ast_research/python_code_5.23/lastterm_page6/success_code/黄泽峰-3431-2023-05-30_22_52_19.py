ls_red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
ls_black = list[range(0,37)] - ls_red
a = eval(input())
if a == 0:
    print("green")
elif a in ls_red:
    print("red") 
elif a in ls_black:
    priny("black")
else:
    print(error)
