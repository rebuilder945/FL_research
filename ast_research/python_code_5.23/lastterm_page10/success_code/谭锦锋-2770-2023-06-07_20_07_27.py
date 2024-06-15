a = input()
b = input()
s = 0
for i in list(a):
    if i in list(b):
        continue
    else:
        s = 1
if s == 0 and len(a)==len(b):
    print("True")
else:
    print("False")
