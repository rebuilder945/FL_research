a1="".join(input())
b1="".join(input())
if len(a1)!=len(b1):
    print("False")
else:
    s=0
    for i in a1:
        if a1.count(i)==b1.count(i):
            s+=1
        else:
            s=0
    if s==len(a1):
        print("True")
    else:
        print('False')
