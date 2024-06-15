a   =   input()
c = ""
for i in a:
    b = (int(i)+5)%10
    c = c+str(b)
print(c[::-1])
