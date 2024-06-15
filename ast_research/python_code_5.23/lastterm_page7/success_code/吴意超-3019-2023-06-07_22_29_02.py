stu = {"name": "Zhang"}

name, eng_score, py_score, math_score = input().split()
stu["english"] = float(eng_score)
stu["python"] = float(py_score)
stu["math"] = float(math_score)

total_score = stu["english"] + stu["python"] + stu["math"]
avg_score = total_score / 3
stu["avg"] = round(avg_score, 2)

sorted_scores = sorted(stu.items(), key=lambda x: x[1], reverse=True)

print(stu["name"], end=' ')
for score in sorted_scores[1:]:
    print("%.2f" % score[1], end=' ')
print()
