
stu = {}
values = input().split()
stu["name"] = values[0]
stu["english"] = float(values[1])
stu["python"] = float(values[2])
stu["math"] = float(values[3])


avg_score = (stu["english"] + stu["python"] + stu["math"]) / 3
stu["avg"] = avg_score

sorted_scores = sorted([stu["english"], stu["python"], stu["math"]], reverse=True)


print(stu["name"], end=" ")
for score in sorted_scores:
    print("{:.2f}".format(score), end=" ")
print("{:.2f}".format(avg_score))
