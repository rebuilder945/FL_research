def encrypt_date(input_number):
    digits=[int(digit) for digit in str(input_number)]
    for i in range(len(digits)):
        digits[i]=(digits[i]+5)%10
    for i in range(len(digits)//2):
        digits[i],digits[-i-1]=digits[-i-1],digits[i]
    encrypted_number = str(''.join(map(str, digits)))
    return encrypted_number
input_number=int(input())
result =encrypt_date(input_number)
print(result)

    

