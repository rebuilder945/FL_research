sum = 0
n = 0
while(1):
    a = input()
    if a!= "#":
        n +=1
        sum = sum+int(a)
    else:
        break
print(n,sum)
