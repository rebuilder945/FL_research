# a = eval(input())

# def getDaff(a:int):
#     m,left= 0,1000
#     if a <= 100:
#         print("none")
#         return
#     elif a < 1000:
#         left = a
#     for i in range(100,left+1):
#         n = 0
#         for x in str(i):
#             p = int(x)
#             n += p**3
#         if n == i:
#             m += 1
#             print(i)
#     if m == 0:
#         print("none")
#         return
# getDaff(a)

a=eval(input())
m=0
if a>100 and a<1000:
    for i in range(100,a+1):
        n=0
        for x in str(i):
            p=int(x)
            n=(p**3)+n
        if n==i:
            m+=1
            print(i)
    if m==0:
        print("none")
elif a>=1000:
    for i in range(100,1000):
        n=0
        for x in str(i):
            p=int(x)
            n=(p**3)+n
            if n==i:
                print(i)
            else:
                continue
elif a<=100:
    print("none")
