s = input()
level = 0
num = 0
xiao = 0
da = 0
special = 0
lst = []
for i in s:
    if i.isdigit():
        num = 1
        lst.append(i)
    elif i.isalpha:
        if i.islower():
            xiao = 1
            lst.append(i)
        elif i.isupper():
            da = 1
            lst.append(i)
level = int(num)+int(xiao)+int(da)
if len(s) >= 8:
    if len(s)>len(lst):
        level += 2
    else:
        level += 1
elif len(s) < 8:
    if len(s)>len(lst):
        level += 1
print(level)
