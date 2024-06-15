n=eval(input())
if n<0:
    print("illegal input")
elif n-int(n)!=0:
    print("illegal input")
else:
    sushu=[]
    for i in range(2,n):
        if n%i==0:
            break
        else:
            sushu.append(i)
    for x in sushu:
        string1=str(x)
        string2=string1[::-1]
        if string1==string2:
            print(x)
        else:
            pass
