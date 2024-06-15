def add_id(data2):
    result = []
    for item in data2:
        if len(item) == 6 and item.isdigit() and item[:2] == "19":
            result.append("20" + item)
        else:
            result.append(item)
    return result


data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

