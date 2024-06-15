lst = eval(input())
z,y = eval(input())
if y  <= len(lst)-2 :
    del lst[z:y]
    print(lst)
    if  y > len(lst)-2:
        print("error")

