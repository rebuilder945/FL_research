s = input()
level = 0
num = 0
xiao = 0
da = 0
special = 0

for i in s:
    if i.isdigit():
        num = 1
    elif i.isalpha:
        if i.islower():
            xiao = 1
        elif i.isupper():
            da = 1
    elif i in "~!@#$%^&*()_=-/,.?<>;:[]{}|":
        special = 1
level = int(num)+int(xiao)+int(da)+int(special)
if len(s) >= 8:
    level += 1
print(level)
