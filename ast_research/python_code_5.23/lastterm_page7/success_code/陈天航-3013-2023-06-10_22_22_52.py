GDP = {}
while True:
    line = input().strip()
    if line == 'ok':
        break
    country, value = line.split()
    GDP[country] = int(value)
keys = sorted(list(GDP.keys()))
values = sorted(list(GDP.values()))
is_india_exist = 'India' in GDP
answer1 = 'yes' if is_india_exist else 'no'
sum_values = sum(GDP.values())
print(keys)
print(values)
print(answer1)
print(sum_values)

