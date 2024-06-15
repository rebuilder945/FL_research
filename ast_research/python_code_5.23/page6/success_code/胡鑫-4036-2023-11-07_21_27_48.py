n = eval(input())
list1 = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
list2 = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
if n == 0:
    print("green")
for i in list1:
    if i == n:
        print("red")
for i in list2:
    if i == n:
        print("black")
if n > 36:
    print("error")
