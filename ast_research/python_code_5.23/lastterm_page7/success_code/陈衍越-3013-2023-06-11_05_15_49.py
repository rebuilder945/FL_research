GDP = {}
while True:
    #line = input().strip()
    #注意不能使用split(),与ok冲突
    line = input()
    if line == 'ok':
        break
    else:
        #创建键值对
        key,value = line.split()
        GDP[key] = eval(value)

lst1 = sorted(list(GDP.keys()))
lst2 = sorted(list(GDP.values()))
print(lst1)
print(lst2)
print('yes' if 'India' in lst1 else 'no')
print(sum(lst2))

# 初始化空字典
data = {}

# 循环读入多行数据
while True:
    line = input().strip()
    if line == 'ok':
        break
    else:
        # 将每行数据按空格分隔成键值对，并存入字典
        key, value = line.split()
        data[key] = int(value)

# 第一行输出所有的key值，按升序排列
keys = sorted(data.keys())
print(' '.join(keys))

# 第二行输出所有的value值，按升序排列
values = sorted(data.values())
print(' '.join(str(v) for v in values))

# 第三行判断键'India'是否在字典中
if 'India' in data:
    print('yes')
else:
    print('no')
    
print(sum(data.values()))
