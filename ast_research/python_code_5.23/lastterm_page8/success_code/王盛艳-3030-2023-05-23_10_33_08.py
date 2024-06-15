name_list = input().split(',')
score_list = list(map(int,input().split(',')))
m = [[name_list[i],score_list[i]] for i in range(len(name_list))]
m.sort(key = lambda x:x[1])
print(m)
