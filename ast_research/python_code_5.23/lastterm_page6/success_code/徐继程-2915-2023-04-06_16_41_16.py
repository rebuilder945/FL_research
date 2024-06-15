num=eval(input())
for i in range(99,num):
    i=str(i)
    a=int(i[0])
    b=int(i[1])
    c=int(i[2])
    if a**3+b**3+c**3==int(i):
        print(int(i))

