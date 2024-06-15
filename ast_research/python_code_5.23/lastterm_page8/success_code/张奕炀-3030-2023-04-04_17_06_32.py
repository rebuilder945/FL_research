name = input().split(",")
answer = input().split(",")
answer = list(map(int,answer))
dic = {}
list0 = []
list1 = []
for i in range(len(name)):
    dic[answer[i]] = name[i]
answer.sort()
for i in range(len(answer)):
    list1.append([dic[answer[i]],answer[i]])
print(list1)
