item  =  input().split()
dic  =  {}
list0 = []
while item != ["ok"]:
    dic[item[0]] = item[1]
    list0.append([item[0],item[1]])
    item = input().split()
list_keys = []
for i in range(len(list0)):
    list_keys.append(list0[i][0])
list_keys.sort()
list_values = []
for i in range(len(list0)):
    list_values.append(int(list0[i][1]))
list_values.sort()
print(list_keys)
print(list_values)
if 'India' in list_keys:
    print("yes")
else:
    print("no")
print(sum(list_values))

