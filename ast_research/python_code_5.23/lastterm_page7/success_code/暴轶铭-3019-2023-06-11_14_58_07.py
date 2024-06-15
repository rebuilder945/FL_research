stu = {"name":"","english":"","python":"","math":""}
stu["name"],stu["english"],stu["python"],stu["math"] = input().split()
scores = []
scores.append(int(stu["english"]))
scores.append(int(stu["python"]))
scores.append(int(stu["math"]))
scores.sort(reverse=True)
avg = "%.2f"%(sum(scores) / len(scores))
print(stu["name"],end=" ")
for i in range(len(scores)):
    print("%.2f"%(scores[i]),end=" ")
print(avg)


