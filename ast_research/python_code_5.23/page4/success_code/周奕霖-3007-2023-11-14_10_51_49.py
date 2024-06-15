lst = eval(input())
z,y = eval(input())
if y <= len(lst):
    del lst[z:y]
    print(lst)
    if y > len(lst):
        print("error")
