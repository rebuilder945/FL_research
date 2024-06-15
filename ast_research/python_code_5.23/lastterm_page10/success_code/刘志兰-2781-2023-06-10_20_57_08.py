def validate_id_card(id_card):
    if len(id_card) != 18:
        return "Error"
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    check_code = "10X98765432"
    sum = 0
    for i in range(17):
        sum += int(id_card[i]) * weight[i]
    remainder = sum % 11
    if check_code[remainder] == id_card[-1]:
        return "Correct"
    else:
        return "Wrong"

id_card = input()
print(validate_id_card(id_card))
