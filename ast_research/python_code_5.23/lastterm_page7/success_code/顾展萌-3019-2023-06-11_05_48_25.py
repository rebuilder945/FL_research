
stu = {"name":"Zhang"}

inp = input().split()

for i in range(1, 4):
    stu[inp[i-1]] = int(inp[i])

avg_score = (stu["english"] + stu["python"] + stu["math"]) / 3
stu["avg"] = avg_score

sort_result = sorted(stu.items(), key=lambda x:x[1], reverse=True)

print(sort_result[0][1], "%.2f" % sort_result[1][1], "%.2f" % sort_result[2][1], "%.2f" % sort_result[3][1], "%.2f" % avg_score)

