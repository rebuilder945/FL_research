def jiami(i):
    b = (i+5)%10
    return b
a = input()
c = ''
for x in a:
    c+=str(jiami(int(x)))
print(c[::-1])
