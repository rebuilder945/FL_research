while True:
name = input())
if name == 'q':
    break
gdp = int(input())
GDP[name] = gdp

print("GDP")
keys = list(GDP.keys())
print( "keys")
values = list(GDP.values())
print( values)



if 'India' in GDP.keys():
print('no')
else:
print('no')

5. 实现代码：

total = sum(GDP.values())
print("total")
