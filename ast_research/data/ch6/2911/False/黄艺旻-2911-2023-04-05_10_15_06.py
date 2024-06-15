a = list(input())
b = ''
for i in a:
    b += str(int(i)+5%10)
print(b)
