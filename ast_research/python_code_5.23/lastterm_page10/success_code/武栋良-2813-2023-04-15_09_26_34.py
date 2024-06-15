m = input()
n = input()
if n not in m:
    print(m)
else:
    m.replace(n,'')
    print(m)
