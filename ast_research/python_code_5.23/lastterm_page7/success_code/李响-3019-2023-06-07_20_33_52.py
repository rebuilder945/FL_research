stu={"name":"Zhang","english":80,"python":90,"math":100}
stu["avg"] = (stu["english"]+stu["python"]+stu["math"])/3
print('{} {:.2f} {:.2f} {:.2f} {:.2f}'.format(stu["name"],stu["english"],stu["python"],stu["math"],stu["avg"]))
