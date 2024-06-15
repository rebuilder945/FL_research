
try:
    pocket_number=int(input())
    if 0<=pocket_number<=36:
        if pocket_number==0:
            color="green"
        elif(1<=pocket_number<=10)or(19<=pocket_number<=28):
            color="red" if pocket_number%2==1 else "black"
        elif(1<=pocket_number<=10)or(19<=pocket_number<=28):
            color="black" if pocket_number%2==1 else "red"
        print(color)
    else:
        print("error")

except:
    print("error")

