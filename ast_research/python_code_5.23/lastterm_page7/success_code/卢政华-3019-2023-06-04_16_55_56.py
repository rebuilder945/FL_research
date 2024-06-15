name, eng, python, math = input().split()
stu = {"name": name, "english": float(eng), "python": float(python), "math": float(math)}
avg=(stu["english"]+stu['python']+stu['math'])/3
stu['avgs']=avg
sorted_scores = sorted([stu["english"], stu["python"], stu["math"]])
print(stu[name],stu[math],stu[python],stu[eng],stu[avg])

