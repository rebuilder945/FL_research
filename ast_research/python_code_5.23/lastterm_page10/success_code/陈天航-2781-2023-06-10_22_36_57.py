id_number = input()
if len(id_number) != 18:
    print("Error")
else:
    factors = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    total = 0
    for i in range(17):
        total += int(id_number[i]) * factors[i]
    remainder = total % 11
    check_code_dict = {0:1, 1:0, 2:'X', 3:9, 4:8, 5:7, 6:6, 7:5, 8:4, 9:3, 10:2}
    if id_number[17] == str(check_code_dict[remainder]):
        print("Correct")
    else:
        print("Wrong")


