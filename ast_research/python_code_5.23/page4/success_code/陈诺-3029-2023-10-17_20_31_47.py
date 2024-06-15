name_list=[]
score_list=[]
result_list=[]
for name,score in zip([name_list,score_list]):
    result_list.append([name,score])
result_list.sort(key=lambda x:x[1])
print(result_list)
