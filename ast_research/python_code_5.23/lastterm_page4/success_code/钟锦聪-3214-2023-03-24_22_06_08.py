num = eval(input())
for x in num:
    if x ==0:
        num.remove(0)
        num.append(0)
print(num)
