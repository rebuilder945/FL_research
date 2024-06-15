dict_mi_ming = {}
print(chr(ord('A')))
for i in range(26):
    mi = chr(ord('a')+i)
    ming=chr(ord('a')+25-i)
    dict_mi_ming[mi]=ming
print(dict_mi_ming['a'])
for i in range(26):
    mi = chr(ord('A')+i)
    ming=chr(ord('A')+25-i)
    dict_mi_ming[mi]=ming
line=input()
result=""
for ch in line :
    if ch.isalpha():
        result +=dict_mi_ming[ch]
    else:
        result +=ch
print(line)
print(result)

