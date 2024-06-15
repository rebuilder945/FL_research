m = input()
n = input()
if len(m) == len(n):
    lst = []
    for i in m:
        if i in n:
            lst.append(i)
    if len(lst) == len(m):
        print("True")
    else:
        print("False")
else:
    print("False")
