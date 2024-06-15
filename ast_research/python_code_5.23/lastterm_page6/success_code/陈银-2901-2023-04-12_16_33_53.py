while True:
    a = input().strip()
    count = 0
    sum = 0
    if a == "#":
        break
    if type(a)== type(1):
        count += 1
        sum+=a
    print(count,sum)

    
