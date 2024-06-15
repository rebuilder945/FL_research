lst = eval(input())
n,m = eval(input())
for x in range(n,m):
    if x>0 and m<(len(lst)-1):
        lst.pop(x)
    else:
        print("error")
print(lst)

