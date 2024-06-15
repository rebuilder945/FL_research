a = eval(input())
a.sort(reverse = True)
b = ''
for i in a:
    if str(i) not in b:
        b = b + str(i)
print(int(b))
        

