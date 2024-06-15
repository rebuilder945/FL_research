str1 = input()
str2 = "~!@#$%^&*()_=-/,.?<>;:[]{}|\ "
xing = 0
if len(str1) >= 8:
    xing = xing +1
for x in str1:
    if 1 <= int(x) <= 9:
        xing = xing + 1
        break
for x in str1:
    if 'a' <= x <= 'z':
        xing = xing + 1
        break
for x in str1:
    if 'A' <= x <= 'Z':
        xing = xing + 1
        break
for x in str1:
    if x in str2:
        xing = xing + 1
        break
print(xing)
