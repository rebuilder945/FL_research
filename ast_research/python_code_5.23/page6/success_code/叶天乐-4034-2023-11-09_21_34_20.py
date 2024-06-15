a = input()
b = input()
ls1 = {red,blue,yellow}
ls2 = {a,b}
ls3 = {red,blue}
ls4 = {red,yellow}
ls5 = {blue,yellow}
if a not in ls1 or b not in ls1 or a==b:
    print("error")
elif ls2 == ls3:
    print("purple")
elif ls2 == ls4:
    print("orange")
elif ls2 == ls5:
    print("green")
    
