a = input()
b = input()
if len(a) != len(b):
    print("False")
elif len(a) == len(b):
    m = 0
    for i in range(0,len(a)):
        for j in range(0,len(b)):
            if a[i] == a[j]:
                m+=1
    if m>=len(a):
        print("True")
    else:
        print("True")
