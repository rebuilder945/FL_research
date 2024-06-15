number=eval(input())
if number>36 or number<0:
    print("error")
else:
    if number==0:
        print("green")
    list1=[x for x in range(1,37,2)]
    list2=[x for x in range(2,37,2)]
    if number in list1:
        if number in range(1,10) or number in range(19,28):
            print("red")
        if number in range(11,18) or number in range(29,36):
            print("black")
    if number in list2:
        if number in range(1,11) or number in range(19,29):
            print("black")
        if number in range(11,19) or number in range(29,37):
            print("red")
