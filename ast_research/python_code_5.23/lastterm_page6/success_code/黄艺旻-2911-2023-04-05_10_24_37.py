a = input()
b = ''
for i in a:
    b += str(int(i)+5%10)
c = list.b
c[0] = c[-1]
c[1] = c[-2]
print(str(c))
