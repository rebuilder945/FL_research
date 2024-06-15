item  =  input()  or  "q"
dic  =  {}
while item != "q":
    if item not in dic.keys():
        dic[item] = 1
    else:
        dic[item] = dic[item] + 1
    item = input() or "q"
list0 = [0,0]
for i in dic:
    if dic[i] > list0[1]:
        list0[0] = i
        list0[1] = dic[i]
list0 = list(map(str,list0))
answer = " ".join(list0)
print(answer)
