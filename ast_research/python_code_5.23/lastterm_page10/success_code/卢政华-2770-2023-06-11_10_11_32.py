a=input()
b=input()
a=list(a)
b=list(b)
a.sort(reverse=False)
b.sort(reverse=False)
if a ==b:
    print("True")
else:
    print("False")
