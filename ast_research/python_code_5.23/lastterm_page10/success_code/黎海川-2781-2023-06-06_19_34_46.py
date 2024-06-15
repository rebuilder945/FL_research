idcard = input()
s = list(idcard)
Checkcode = {'0':'1','1':' 0','2': 'X','3': '9','4': '8','5': '7','6': '6','7': '5','8': '4','9': '3','10': '2'}
if len(s) != 18:
    print("Error")
else:
    m = s[0] * 7 + s[1] * 9 + s[2] * 10 + s[3] * 5 + s[4] * 8 + s[5] * 4 + s[6] * 2 + s[7] * 1 + s[8] * 6 + s[9] * 3 + s[10] * 7 + s[11] * 9 + s[12] * 10 + s[13] * 5 + s[14] * 8 + s[15] * 4 + s[16] * 2
    l=str(m)
    n = l % 11
if Checkcode["n"] == s[17]:
    print("Correct")
else:
    print("Error")

    
