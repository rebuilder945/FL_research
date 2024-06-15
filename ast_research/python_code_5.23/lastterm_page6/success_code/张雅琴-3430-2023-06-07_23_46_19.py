a=eval(input())
if a<1 or a>12:
    print("error")
else:
    if 3<=a<=5:
        print("spring")
    elif 6<=a<=8:
        print("summer")
    elif 9<=a<=11:
        print("autumn")
    else:
        print('winter')
