seasons = [(3, 4, 5, 'spring'), (6, 7, 8, 'summer'), (9, 10, 11, 'autumn'), (12, 1, 2, 'winter')]

month = input().strip()

if not month.isdigit():
    print('error')
else:
    month = int(month)
    if month < 1 or month > 12:
        print('error')
    else:
        for s in seasons:
            if month in s[:-1]:
                print(s[-1])
                break

