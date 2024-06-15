num = input()
new_num = []
for i, n in enumerate(num): 
    new_n = (int(n) + 5) % 10    
    new_num.append(str(new_n))
for i in range(len(new_num) // 2):    
    new_num[i], new_num[-i-1] = new_num[-i-1], new_num[i]
print((new_num))

