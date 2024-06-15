def add_id(data2):
    
    wrong_numbers = input()
    numbers_list = wrong_numbers.split()
    for number in numbers_list:
        if len(number) == 6:
            correct_number = "20" + number
            print(correct_number)
        else:
            print(number)

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

