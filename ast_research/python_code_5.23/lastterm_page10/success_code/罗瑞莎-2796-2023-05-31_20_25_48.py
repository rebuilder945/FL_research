s = input()
a = []
n = []
for i in s:
    if i.isalpha():
        n = []
    elif i.isdigit():
        n.append(i)
        if len(a) < len(n):
            a = n
if a == 0:
    print("No digits")
else:
    print("".join(a))
