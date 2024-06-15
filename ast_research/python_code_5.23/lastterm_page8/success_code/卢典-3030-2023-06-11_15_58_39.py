names = input().split(',')
scores = list(map(int, input().split(',')))
combo_list = []
for i in range(len(names)):
    combo_list.append([names[i], scores[i]])
sorted_list = sorted(combo_list, key=lambda x: x[1])
print(sorted_list)
