#本题目要求读入一个字符串，输出字符串的最长数字子串。
#输出最长数字子串，若有多个最长数字子串输出最后一个，若字符串无数字字符，则输出“No digits”。
s = input()
maxzichuan = 0
zichuan = 0
dic = {}
a = ""
ls = []
for i in s:
    if "0"<= i<= "9":
        a += i
    else:
        dic[a] = len(a)
        a = ""
if dic=={}:
    print("No digits")
else:
    max_value= max(dic.values())
    for m,n in dic.items():
        if n == max_value:
            ls.append(m)
    print(ls[-1])
      

