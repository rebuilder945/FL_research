strings=input()
string_list=list(strings)
for i in range(len(string_list)):
    if ord('A')<=ord(string_list[i])<=ord('Z'):
        x=ord('A')+25-(ord(string_list[i])-ord('A'))
        string_list[i]=chr(x)
    elif ord('a')<=ord(string_list[i])<=ord('z'):
        x=ord('a')+25-(ord(string_list[i])-ord('a'))
        string_list[i]=chr(x)
string=''.join(string_list)
print(strings)
print(string)
