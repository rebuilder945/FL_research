id_num = input()
if len(id_num) != 18:
    print("Error")
else:
    factors = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    check_codes = {0: '1', 1: '0', 2: 'X', 3: '9', 4: '8', 5: '7', 6: '6', 7: '5', 8: '4', 9: '3', 10: '2'}
    sum = 0
    for i in range(len(factors)):
        sum += int(id_num[i]) * factors[i]
    remainder = sum % 11
    if id_num[-1] == check_codes[remainder]:
        print("Correct")
    else:
        print("Wrong")



