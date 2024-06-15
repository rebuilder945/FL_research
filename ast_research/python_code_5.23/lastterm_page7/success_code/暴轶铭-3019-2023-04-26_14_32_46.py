stu = {"name": "", "english": 0, "python": 0, "math": 0}

stu["name"] = input("")
stu["english"] = float(input(""))
stu["python"] = float(input(""))
stu["math"] = float(input(""))

average_score = round((stu["english"] + stu["python"] + stu["math"]) / 3, 2)
stu["avg"] = average_score

sorted_scores = sorted([(k, v) for k, v in stu.items() if k != "name"],
                       key=lambda x: x[1], reverse=true)

print(f"{stu['name']}")
for item in sorted_scores:
    print(f"{item[0]}：{item[1]:.2f}")
print(f"{average_score:.2f}")
