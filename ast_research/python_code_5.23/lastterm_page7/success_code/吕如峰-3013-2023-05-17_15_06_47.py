GDP = {}
while True:
    user_input = input()
    if user_input == 'ok':
        if not GDP:
            print('GDP字典不能为空')
            continue
        break
    nation,gdp = user_input.split()
    GDP[nation] = int(gdp)
print(GDP)
