name=input().split(",")
score=input().split(",")
result_list=[]
for i,j in zip(name,score):
    result_list.append([i,j])
result_list.sort(key=lambda x:x[1])
print(result_list)
