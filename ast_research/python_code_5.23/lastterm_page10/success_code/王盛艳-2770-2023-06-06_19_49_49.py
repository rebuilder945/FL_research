a = input()
b = input()
s = 0
for i in a:
    if i in b:
        continue
    else:
        s += 1
if s == 0 and len(a) == len(b):
    print("True")
else:
    print("False")
