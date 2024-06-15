s_list = input().split()
num_list=[]
for i in s_list:
    num_list.append(s_list.count(i))
max_num = max(num_list)
dic={}

for i in range(len(s_list)):
    dic[s_list[i]]=num_list[i]
def find_max(dic,max_num):
    print(max(dic, key=dic.get), max_num)
    del dic[max(dic, key=dic.get)]
    num_list.pop(max_num)
    max_num1=max(num_list)
    return max_num1



while True:
    max_num1=find_max(dic,max_num)
    if max_num1 == max_num:
        find_max(dic,max_num1)
    else:
        break


