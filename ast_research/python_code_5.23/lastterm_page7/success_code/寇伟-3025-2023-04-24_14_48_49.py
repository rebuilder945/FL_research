s_list = input().split()
num_list=[]
for i in s_list:
    num_list.append(s_list.count(i))
max_num = max(num_list)
dic={}
for i in range(len(s_list)):
    dic[s_list[i]]=num_list[i]
def find_max():
    print(max(dic, key=dic.get), max_num)
    del dic[max(dic, key=dic.get)]
    num_list.pop(max_num)



while True:
    if max_num1 == max_num:
        find_max()
    else:
        break


