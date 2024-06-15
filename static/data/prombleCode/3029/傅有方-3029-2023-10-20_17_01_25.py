name_list=['tom''jack''jone''mike']
score_list=[88,89,34,90]
result_list=[]
for name,score in zip(name_list,score_list):
    result-list.append([name,score])
result_list.sort(key=lambda x:x[1])
print(result_list)
