stu={ "name":"Zhang","english":80,"python":90,"math":100 }
name = "Zhang"
english_score = 80
python_score = 90
math_score = 100

stu["name"] = name
stu["english"] = english_score
stu["python"] = python_score
stu["math"] = math_score
total_score = stu["english"] + stu["python"] + stu["math"]
avg_score = total_score / 3

stu["avg"] = avg_score
sorted_scores = sorted(list(stu.values())[1:], reverse=True)
print(f"Name: {stu['name']}")
print(f"English score: {stu['english']:.2f}")
print(f"Python score: {stu['python']:.2f}")
print(f"Math score: {stu['math']:.2f}")
print(f"Average score: {stu['avg']:.2f}")

