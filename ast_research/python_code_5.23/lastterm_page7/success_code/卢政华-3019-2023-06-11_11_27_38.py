name, eng, python, math = input().split()
stu = {"name": name, "english": float(eng), "python": float(python), "math": float(math)}
avg=(stu["english"]+stu['python']+stu['math'])/3
stu['avgs']=avg
sorted_scores = sorted([stu["english"], stu["python"], stu["math"]])
print("{} {:.2f} {:.2f} {:.2f} {:.2f}".format(name,sorted_scores[0],sorted_scores[1],sorted_scores[2],avg))
