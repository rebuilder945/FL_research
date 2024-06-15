s = eval(input())
jishu = [0]*26
for x in s:
    for zimu in x:
        jishu[ord(zimu) - ord('a')]+=1

for i in range(26):
    if jishu[i]>0:
        print(chr(i + ord('a')) + "," + str(jishu[i]))
