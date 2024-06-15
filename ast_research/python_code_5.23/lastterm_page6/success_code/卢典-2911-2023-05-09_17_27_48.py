num = input() 
encrypted_num = [(int(i) + 5) % 10 for i in num]
for i in range(len(encrypted_num) // 2):
    encrypted_num[i], encrypted_num[-i-1] = encrypted_num[-i-1], encrypted_num[i]
print("".join(map(str, encrypted_num)))

