id_number = input()
if len(id_number) != 18:
    print("Error")
else:
    coefficients = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    check_codes = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    sum = 0
    for i in range(17):
        sum += int(id_number[i]) * coefficients[i]
    remainder = sum % 11
    if id_number[-1] == check_codes[remainder]:
        print("Correct")
    else:
        print("Wrong")

        
        
            

