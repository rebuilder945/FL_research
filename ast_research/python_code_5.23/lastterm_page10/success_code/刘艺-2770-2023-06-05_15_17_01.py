a = input()
b = input()
liu = 0
if len(a) != len(b):
    print("False")
if len(a) == len(b):
    for i in range(0,len(a)):
        for j in range(0,len(b)):
            if a[i] == b[j]:
                liu += 1
    if liu == len(a):
        print("True")
    else:
        print("False")

