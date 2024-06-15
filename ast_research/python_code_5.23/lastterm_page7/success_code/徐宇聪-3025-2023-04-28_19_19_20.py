string_count = {}

for s in input().split():
    if s in string_count:
        string_count[s] += 1
    else:
        string_count[s] = 1

max_count = 0
max_string = ''
for string , count in string_count.items():
    if count > max_count:
        max_count = count
        max_string = string

for string , count in sorted(string_count.items()):
    if count == max_count:
        print('{} {}'.format(string,count))
