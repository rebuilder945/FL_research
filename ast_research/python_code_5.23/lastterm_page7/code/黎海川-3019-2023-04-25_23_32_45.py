name, eng, python, math = input().split()
stu['name'] = name
stu['english'] = int(eng)
stu['python'] = int(python)
stu['math'] = int(math)


avg = (stu['english'] + stu['python'] + stu['math']) / 3
stu['avg'] = round(avg, 2)

sorted_scores = sorted(stu.values(), reverse=True)[1:]

print(stu['name'], end=' ')
for score in sorted_scores:
print('{:.2f}'.format(score), end=' ')
print('{:.2f}'.format(stu['avg']))
