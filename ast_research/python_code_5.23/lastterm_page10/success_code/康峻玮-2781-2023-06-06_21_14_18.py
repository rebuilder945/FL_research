id_number = input()
if len(id_number) != 18:
    print("Error")
else:
    factors = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    sum_product = 0
    for i in range(17):
        sum_product += int(id_number[i]) * factors[i]
    remainder = sum_product % 11
    check_codes = {0: 1, 1: 0, 2: "X", 3: 9, 4: 8, 5: 7, 6: 6, 7: 5, 8: 4, 9: 3, 10: 2}
    if check_codes[remainder] == id_number[-1]:
        print("Correct")
    else:
        print("Wrong")
