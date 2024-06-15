s = input()  
if not s:  
    print("None")  
else:  
    for i in range(len(s)):  
        if s.count(s[i]) == 1:  
            print(s[i])  
            break
