m=eval(input())
l,r=eval(input())
n=len(m)
while s>l:
    if l>=n or r>=n:
        print("error")
        break
    del m[l]
else:
    print("error")

