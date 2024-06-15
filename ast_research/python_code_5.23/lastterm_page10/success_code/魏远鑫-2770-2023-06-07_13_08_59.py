n=input()
m=input()
if list(n).sort()==list(m).sort():
    print("True")
elif len(n)!=len(m):
    print("False")
else:
    print("False")
