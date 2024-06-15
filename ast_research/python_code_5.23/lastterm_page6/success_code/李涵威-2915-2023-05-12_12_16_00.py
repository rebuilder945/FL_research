n = eval(input())
flag = False
for i in range(100,n+1):
    a = i%10
    b = ((i-a)/10)%10
    c = ((i-a-10*b)/100)
    if a**3+b**3+c**3 == i:
        print(i)
        flag = True
if flag is False:
    print("none")
