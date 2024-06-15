id_num = input()


if len(id_num) != 18:
    print("Error")
else:
   
    factors = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    check_codes = "10X98765432"

   
    total = 0
    for i in range(17):
        total += int(id_num[i]) * factors[i]
    remainder = total % 11
    check_code = check_codes[remainder]

   
    if check_code == id_num[-1]:
        print("Correct")
    else:
        print("Wrong")






