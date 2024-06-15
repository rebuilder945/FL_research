GDP = {

'USA': 95,

'China': 80,

'Japan': 50

}
k_list=[]
v_list=[]
for k,v in GDP.items():
    k_list.append(k)
    v_list.append(v)
    k_list.sort(reverse=True)
print(k_list)
print(sorted(v_list))
if 'India'not in k_list:
    print('no')
else:
    print('yes')
print(sum(v_list))


