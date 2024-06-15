name, eng, python, math = input().split()
stu = {"name": name, "english": float(eng), "python": float(python), "math": float(math)}
avg=(stu["english"]+stu['python']+stu['math'])/3
stu['avgs']=avg
sorted_scores = sorted([stu["english"], stu["python"], stu["math"]])
print("%s %.2f%.2f%.2f%.2f"%(stu["name"],stu["math"],stu["python"],stu["english"],stu["avgs"]))

