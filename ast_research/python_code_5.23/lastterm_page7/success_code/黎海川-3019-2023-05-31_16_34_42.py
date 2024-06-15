name, english, python, math = input().split(' ')
stu = {
    'name': name, 
    'english': float(english),
    'python': float(python),
    'math': float(math),
    'avg': sum([float(english), float(python), float(math)]) / 3
}

print(stu['name'], end=' ')
for item in sorted([stu['english'], stu['python'], stu['math']], reverse=True):
    print('%.2f' % item, end=' ')
print(f"{stu['avg']:.2f}")
 
