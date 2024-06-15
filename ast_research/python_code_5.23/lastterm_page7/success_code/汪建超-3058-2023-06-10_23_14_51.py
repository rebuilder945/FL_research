# str_dict = {}
# while True:
#     s = input().strip()
#     if s == 'q':
#         break
#     if s in str_dict:
#         str_dict[s] += 1
#     else:
#         str_dict[s] = 1
# max_str = max(str_dict, key=str_dict.get)
# print(max_str, str_dict[max_str])
x={}
s=input()
while s!='q':
    x[s]=x.get(s,0)+1
    s=input()
print(max(x,key=x.get),end=' ')
print(max(x.values()))

