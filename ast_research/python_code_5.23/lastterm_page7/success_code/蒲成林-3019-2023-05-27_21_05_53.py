name, english, python, math = input().split()
english = float(english)
python = float(python)
math = float(math)

stu = {'name': name, 'english': english, 'python': python, 'math': math}
avg = (english + python + math) / 3
stu['avg'] = avg

scores = [english, python, math]
scores.sort(reverse=True)

print(f"{name} {scores[0]:.2f} {scores[1]:.2f} {scores[2]:.2f} {avg:.2f}")
