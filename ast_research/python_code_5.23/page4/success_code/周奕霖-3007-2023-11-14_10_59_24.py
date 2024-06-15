lst = eval(input())
z,y = eval(input())
if y  <= len(lst)-2 or y > z:
    del lst[z:y]
    print(lst)
    if  z > y or y > len(lst)-2:
        print("error")

