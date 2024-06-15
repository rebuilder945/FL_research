lst = eval(input())
z,y = eval(input())
if y  <= len(lst) or y > z:
    del lst[z:y]
    print(lst)
else:
    print("error")
