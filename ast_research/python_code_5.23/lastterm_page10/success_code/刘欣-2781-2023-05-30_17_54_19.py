id_card = input()

if len(id_card) != 18: 
    print("Error")
else:
    factors = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2] 
    last_digit_map = {0:1, 1:0, 2:'X', 3:9, 4:8, 5:7, 6:6, 7:5, 8:4, 9:3, 10:2} 
    sum = 0 
    for i in range(17): 
        sum += int(id_card[i])*factors[i]
    remainder = sum % 11 
    if str(last_digit_map[remainder]) == id_card[-1]: 
        print("Correct")
    else:
        print("Wrong")
