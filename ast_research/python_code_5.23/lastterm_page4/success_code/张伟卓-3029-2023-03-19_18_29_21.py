names = input().split(',')
scores = input().strip('[]').split(',')
new_list = []
for i in range(len(names)):
    new_list.append([names[i], int(scores[i])])
print(new_list)
