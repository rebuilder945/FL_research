line = input
count = 0
length = 0
temp = []
dig = []
for ch in line:
    if (ch >= '0' and ch <= '9'):
        count += 1
        temp.apppend(ch)
    else:
        if count >= length:
            length = count
            count = 0
            dig = temp.copy()
            temp = []
    if len(temp) >= len(dig):
        result = ''.join(temp)
    else:
        result = ''.join(dig)
    if len(result) >0:
        print(result)
    else:
        print("No digits")
