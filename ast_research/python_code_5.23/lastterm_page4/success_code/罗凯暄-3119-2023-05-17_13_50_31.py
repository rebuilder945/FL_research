list = eval(input())
postlist = {}
for i in range(len(list)):
    if list[i] in postlist:
        postlist[list[i]] = i
    else:
        postlist[list[i]] = i
newlist = []
for i in range(len(list)):
    if i == postlist([list[i]]):
        newlist.append(list[i])
print(newlist)

