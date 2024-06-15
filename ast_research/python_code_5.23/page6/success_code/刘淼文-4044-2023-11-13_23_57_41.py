n = eval(input())
for i in range(0,n+1):
    i = str(i)
    a = int(i[0])
    b = int(i[1])
    c = int(i[2])
    s = ""
    if a**3+b**3+c**3==int(i):
        print(i)
    else:
        print("none")

   
