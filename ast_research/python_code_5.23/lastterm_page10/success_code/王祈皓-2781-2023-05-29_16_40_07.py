def validate_id_number(id_number):
    if len(id_number) != 18:
        return "Error"

    factors = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    checksum = sum(int(id_number[i]) * factors[i] for i in range(17))
    remainder = checksum % 11

    mapping = {0: 1, 1: 0, 2: "X", 3: 9, 4: 8, 5: 7, 6: 6, 7: 5, 8: 4, 9: 3, 10: 2}
    if str(mapping[remainder]) == id_number[17]:
        return "Correct"
    else:
        return "Wrong"
id_number = input()
result = validate_id_number(id_number)
print(result)
