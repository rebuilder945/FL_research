n=input()
list1="~!@#$%^&*()_=-/,.?<>;:[]{}|\]"
level=0
for i in n:
    if i in "1234567890":
        level+=1
        break
for i in n:
    if i in "abcdefghijklmnopqrstuvwxyz":
        level+=1
        break
for i in n:
    if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        level+=1
        break
if len(n)>=8:
    level+=1
for i in n:
    if i in list1:
        level+=1
        break
print(level)
