stu={"name","english","python","math"}
stu["name"],stu["english"],stu["python"],stu["math"]=input().split()
average = (int(stu["english"])+int(stu["python"])+int(stu["math"]))/3
stu["avg"]=average
sorted_scores = sorted(stu.items(),key=lambda item:item[1],reverse=True)
print(sorted_scores[0][1], end=' ')
for i in range(1, 4):
    print("%.2f" % sorted_scores[i][1], end=" ")
print("%.2f" % average)
