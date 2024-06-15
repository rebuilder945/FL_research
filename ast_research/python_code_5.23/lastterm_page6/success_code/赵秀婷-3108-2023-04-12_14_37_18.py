lst = eval(input())

count_dict = {}
for i in range(97, 123):
    count_dict[chr(i)] = 0

for s in lst:
    for c in s:
        count_dict[c] += 1

for i in range(97, 123):
    print("{}:{}".format(chr(i), count_dict[chr(i)]))
