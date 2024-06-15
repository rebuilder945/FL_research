lst = eval(input())
n,m = eval(input())
for x in range(n,m+1):
    if x>0 and x<(len(lst)-1):
        lst.pop(x)
    else:
        print("error")
print(lst)

