lst = eval(input())
z,y = eval(input())
if y  <= len(lst) or y > z:
    del lst[z:y]
    print(lst)
    if  z > y or y > len(lst):
        print("error")

