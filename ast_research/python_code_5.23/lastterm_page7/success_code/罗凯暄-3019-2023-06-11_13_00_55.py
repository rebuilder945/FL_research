stu={"name":"Zhang","english":0,"python":0,"math":0}
name, english, python, math = input().split()
stu["name"] = name
stu["english"] = int(english)
stu["python"] = int(python)
stu["math"] = int(math)

avg = (stu["english"] + stu["python"] + stu["math"]) / 3
stu["avg"] = avg

sorted_scores = sorted([stu["english"], stu["python"], stu["math"]], reverse=True)

print(stu["name"], end=" ")
for score in sorted_scores:
    print("{:.2f}".format(score), end=" ")
print("{:.2f}".format(stu["avg"]))

