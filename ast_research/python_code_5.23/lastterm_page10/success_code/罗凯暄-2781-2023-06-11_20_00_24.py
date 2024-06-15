def verify_id(id):
    if len(id) != 18:
        a="Error"
        return a
    factor = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    check_code = '10X98765432'
    total = 0
    for i in range(17):
        total += int(id[i]) * factor[i]
    remainder = total % 11
    if id[-1] == check_code[remainder]:
        a="Correct"
        return a
    else:
        a="Wrong"
        return a
n=input()
print(verify_id(n))

