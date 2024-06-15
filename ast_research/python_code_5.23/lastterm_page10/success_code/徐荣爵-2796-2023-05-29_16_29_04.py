
s = input()
key = 0
#判断是否有数字
for i in range(10):
    if str(i) in s:
        key = 1
#提取数字
for i in range(len(s)):
    if s[i].isdigit():
        pass
    else:
        s = s.replace(s[i],'a')
lst = s.split('a')

max1 = 0
for i in lst:
    j = len(i)
    if j > max1:
        max1 = j
lst2 = []
for i in lst:
    if len(i) == max1:
        lst2 += [i]
if key != 1:
    print('No digits')
else:
    print(lst2[-1])





