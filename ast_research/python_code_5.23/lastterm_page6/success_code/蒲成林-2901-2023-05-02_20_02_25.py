sum=0
ge=0
while True:
    s = input()
    if s == "#":
        break
    else:
        s=int(s)
        sum += s
        ge += 1

print(ge,sum)
    
