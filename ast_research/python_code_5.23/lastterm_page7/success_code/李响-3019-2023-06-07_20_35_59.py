stu={}
stu['name'] = eval(input())
stu['english'] = eval(input())
stu['python'] = eval(input())
stu['math'] = eval(input())
stu["avg"] = (stu["english"]+stu["python"]+stu["math"])/3
print('{} {:.2f} {:.2f} {:.2f} {:.2f}'.format(stu["name"],stu["english"],stu["python"],stu["math"],stu["avg"]))
