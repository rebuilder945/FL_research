n=eval(input())
if type(n) == int and n>1:
    for i in range(0,n+1):
        if str(i)==str(i)[::-1]:
            print(i)
else:
    print("illegal input")
