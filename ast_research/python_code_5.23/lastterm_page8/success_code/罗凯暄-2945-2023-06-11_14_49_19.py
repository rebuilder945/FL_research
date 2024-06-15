def add_id(data2):
        result = []
        for id in data2:
            correct_id = "20" + id
            result.append(correct_id)
        return result


data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

