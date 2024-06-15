a = input()
b = []
for i in range(len(a)):
    b.append((int(b[i])+5)%10)
for i in range(len(b)//2):
    c = b[i]
    b[i] = b[-i-1]
    b[-i-1] = c
for i in range(len(b)):
    print(b[i],end="")
