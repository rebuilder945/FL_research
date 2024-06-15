lst = eval(input())
n,m = eval(input())
for x in range(n,m):
    if x>0 and x<(len(lst)-1):
        lst.pop(x)
        print(lst)
    else:
        print("error")

