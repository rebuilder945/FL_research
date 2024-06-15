idcard = input()
s = list(idcard)
b = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
Checkcode = {'0':'1','1':' 0','2': 'X','3': '9','4': '8','5': '7','6': '6','7': '5','8': '4','9': '3','10': '2'}
if len(s) != 18:
    print("Error")
else:
    sum=0
    for i in range(len(b)):
        sum += int(s[i]) * b[i]
    n = sum % 11
if Checkcode["n"] == s[17]:
    print("Correct")
else:
    print("Error")

    
