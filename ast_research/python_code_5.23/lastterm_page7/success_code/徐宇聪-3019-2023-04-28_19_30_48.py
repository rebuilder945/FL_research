def process_scores(lines):
    stu = {"name":line[0],"english":float(line[1]),"python":float(line[2]),"math":float(line[3])}
    stu1 = stu.copy()
    del stu1["name"]

    avg = sum(stu1.values())/3
    stu["avg"] = avg

    sorted_scores = sorted(stu1.items(), key = lambda x:x[1],reverse = True)
    print(stu["name"],end = ' ')
    for score in sorted_scores[0:]:
        print('{:.2f}'.format(score[1]), end = ' ')
    print('{:.2f}'.format(avg))

line = input().split()
process_scores(line)
