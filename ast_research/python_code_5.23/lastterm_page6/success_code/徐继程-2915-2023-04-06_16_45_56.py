num=eval(input())
for i in range(99,num):
    i=str(i)
    a=eval(i[0])
    b=eval(i[1])
    c=eval(i[2])
    if a**3+b**3+c**3==int(i):
        print(int(i))

