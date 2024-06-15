a = eval(input())
Zero = a.count(0)
while a.count(0) > 0:
    a.remove(0)
Zeros = [0]*Zero
b = a+Zeros
print(b)

