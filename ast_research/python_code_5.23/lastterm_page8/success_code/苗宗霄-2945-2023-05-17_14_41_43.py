def add_id(data2):
        result = []
        for d in data:
            if len(d) == 6 and d[:2] == "20":
                correct_id = "20" + d
                result.append(correct_id)
            else:
                result.append(d)
        return result

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

