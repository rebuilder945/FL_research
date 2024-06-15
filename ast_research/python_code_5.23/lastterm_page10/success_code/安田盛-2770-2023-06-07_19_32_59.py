s=list(input())
d=list(input())
if len(s)==len(d):
    if set(s)==set(d):
        print("True")
    else:
        print("False")
else:
    print("False")


