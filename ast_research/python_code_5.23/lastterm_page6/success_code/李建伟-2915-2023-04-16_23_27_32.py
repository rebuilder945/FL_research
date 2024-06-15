n = input()
if n < 153:
    print("none")
else:
    for i in range(n+1):
        a = int(i[0])
        b = int(i[1])
        c = int(i[2])
        if a*3 + b*3 +c*3 == i:
            print(n)
            


