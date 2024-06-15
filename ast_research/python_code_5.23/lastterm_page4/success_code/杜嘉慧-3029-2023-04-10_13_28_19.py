name = input().split(',')
score = eval(input())
lst = []
pos = 0
for now in name:
    
    lst.append([now, score[pos]])
    pos += 1
print(lst)

