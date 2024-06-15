def add_id(data2):
    for x in data2:
        if len(x)==6:
            correct_number='20'+x
            print(correct_number)
        else:
            print(x)

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

