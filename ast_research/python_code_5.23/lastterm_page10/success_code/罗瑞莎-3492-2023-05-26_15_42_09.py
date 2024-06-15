s = input()
if s == '':
    print("None")
else:
    lst = []
    for i in s:
        if s.count(i)==1:
            lst.append(i)
    print(lst[0])
