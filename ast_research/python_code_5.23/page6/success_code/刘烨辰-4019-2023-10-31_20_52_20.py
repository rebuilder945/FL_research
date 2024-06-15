def lock():
    b=''
    for i in range(0,len(a)):
        b=str((int(a[i])+5)%10)+b
    print(b)
a = input()
lock()  
