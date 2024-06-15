lst = eval(input())
z,y = eval(input())
if y <= len(lst)-1:
    del lst[z:y]
    print(lst)
else:
    print("error")
