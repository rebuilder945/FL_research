def encrypt_number(number):
    number_str=str(number)
    encrypted_number=[]
    for i in range(len(number_str)):
        digit=int(number_str[i])
        digit=(digit+5)%10
        encrypted_number.append(digit)
    encrypted_number[0],encrypted_number[-1]=encrypted_number[-1],encrypted_number[0]
    for i in range(1,len(encrypted_number)//2):
        encrypted_number[i],encrypted_number[-(1+i)]=encrypted_number[-(1+i)],encrypted_number[i]
    encrypted_result=int(''.join(map(str,encrypted_number)))
    return encrypted_result
def main():
    number=str(input())
    a=str(encrypt_number(number))
    print(a)
main()
