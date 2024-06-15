names = input()
score = eval(input())
names2 = names.split(",")
end = []
for i in range(len(score)):
    fin = []
    fin.append(names2[i])
    fin.append(score[i])
    end.append(fin)
print(end)
