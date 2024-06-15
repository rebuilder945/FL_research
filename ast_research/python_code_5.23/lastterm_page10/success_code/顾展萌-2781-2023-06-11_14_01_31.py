
def verify_id(id_str):
    if len(id_str) != 18:
        return 'Error'
    
    factors = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    check_codes = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    checksum = 0

    for i in range(17):
        checksum += int(id_str[i]) * factors[i]

    remainder = checksum % 11
    if check_codes[remainder] == id_str[-1]:
        return 'Correct'
    else:
        return 'Wrong'

id_str = input().strip()
print(verify_id(id_str))

