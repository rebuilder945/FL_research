Ist=eval(input())
n,m=input()
k=len(Ist)
if n>k or m>k:
    print("error")
else:
    del Ist[n:m]
    print(Ist)
