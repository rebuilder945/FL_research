m=eval(input())
l,r=eval(input())
n=len(m)
while r>l:
    if l>=n or r>=n:
        print("error")
        break
    del m[l-1]
    l+=1
if l>=n or r>=n:
    print("error")
else:       
    print(m)

