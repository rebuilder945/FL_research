s = input()
lst = []
for i in s:
    if s.count(i) == 1:
        lst.append(i)
if lst != []:
    print(lst[0])
else:
    print("None")
