count = 0
total = 0
n = ""
while True:
    n = input()
    if n == "#":
        break
    count = count+1
    total += eval(n)
print(count,total)
