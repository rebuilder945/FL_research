a = eval(input())
b = a + 1
s = [x for x in range(1,b)]
del s[0]
s.append(1)
print(s)
