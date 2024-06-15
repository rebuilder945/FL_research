names = input().split(',')
scores = input()[1:-1].split(',')
combo_list = []
for i in range(len(names)):
    combo_list.append([names[i], int(scores[i])])
print(combo_list)
