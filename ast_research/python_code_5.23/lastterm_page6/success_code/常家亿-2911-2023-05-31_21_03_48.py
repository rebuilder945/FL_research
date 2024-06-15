n = input()
lst = []
for i in range(len(n)):
    lst.append((int(n[i])+5)%10)
lst.reverse()
print("".join(str(x) for x in lst))
