lst = eval(input())
z,y = eval(input())
if y and z <= len(lst):
    del lst[z:y]
    print(lst)
    if y and z > len(lst):
        print("error")
