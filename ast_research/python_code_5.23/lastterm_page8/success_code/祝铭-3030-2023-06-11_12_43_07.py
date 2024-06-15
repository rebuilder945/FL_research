name = input().split(',')
mark = input().split(',')
fin = []
for i in range(len(name)):
    mark[i] = int(mark[i])
    fin.append([name[i],mark[i]])
fin.sort(key= lambda x: x[1])
print(fin)
