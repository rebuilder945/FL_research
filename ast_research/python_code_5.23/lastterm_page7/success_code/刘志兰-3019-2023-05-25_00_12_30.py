name, english, python, math = input().strip().split()
english, python, math = int(english), int(python), int(math)
stu={}
stu.update({"name": name, "english": english, "python": python, "math": math})
avg = round(sum([stu["english"], stu["python"], stu["math"]]) / 3, 2)
stu.update({"avg": avg})
sorted_scores = sorted([stu["english"], stu["python"], stu["math"]], reverse=True)
print("{} {:.2f} {:.2f} {:.2f} {:.2f}".format(stu["name"], *sorted_scores, stu["avg"]))
