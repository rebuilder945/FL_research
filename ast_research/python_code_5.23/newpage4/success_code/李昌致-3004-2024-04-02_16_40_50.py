list = eval(input())
i = 0
newlist = []
while i < len(list):
    if list[i] == 0 or list[i] == 1:
        i = i+1
        continue
    if list[i] == 2:
        newlist.append(2)
        i = i+1
        continue
    x = 2
    while x <= list[i]:
        a = list[i]/x
        x = x+1
        if x == list[i]:
            x = 2
            i + i+1
            newlist.append(list[i])
        elif type(a) == int:
            x = 2
            i = i+1
            continue
print(newlist)
        

