c = 0
for i in range (10000):
    a = input()
    if a != "#":
        c += int(a)
    else:
        print(i)
        print(c)
        break
        


