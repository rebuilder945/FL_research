a=input()
if  "." in a:
    print("illegal input")
elif  "-" in a:
    print("illegal input")
elif a=="1":
    print("illegal input")
elif a=="0":
    print("illegal input")
else:
    nums=[]
    for x in range(2,int(a)+1):
        if x ==2:
            nums.append(x)
        if str(x)==str(x)[::-1]:
            for i in range(2,x):
                if x%i==0:
                    break
                else:
                    if i==x-1:
                        nums.append(x)
                    else:
                        continue
        else:
            continue
    print(" ".join(str(q) for q in nums))
