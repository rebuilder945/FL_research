# 1. Read input and store GDP values in a dictionary
GDP = {}
while True:
    input_str = input().strip()
    if input_str == "ok":
        break
    else:
        country, gdp = input_str.split()
        GDP[country] = int(gdp)

# 2. Get all keys and values, and sort them
keys = sorted(list(GDP.keys()))
values = sorted(list(GDP.values()))

# 3. Check if the key 'India' exists in the dictionary
if 'India' in GDP:
    print('yes')
else:
    print('no')

# 4. Calculate the sum of all values in the dictionary
sum_values = sum(GDP.values())

# Output the results
print(keys)
print(values)
print(sum_values)
