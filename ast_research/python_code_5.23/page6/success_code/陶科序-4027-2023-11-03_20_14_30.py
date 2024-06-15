c = 0
for i in range (1,10000):
    a = input()
    if a != "#":
        c += int(a)
    else:
        print(i)
        print(c)
        


