def process_scores(line):
    # 将输入字符串按照空格分割，并存储到一个字典中
    stu = {"name": line.split()[0], "english": float(line.split()[1]), "python": float(line.split()[2]), "math": float(line.split()[3])}
    # 根据字典中的成绩计算平均成绩，并将其添加到字典中
    avg = sum(stu.values() - stu["name"]) / 3
    stu["avg"] = avg
    # 对字典中的成绩进行排序
    sorted_scores = sorted(stu.items(), key=lambda x: x[1], reverse=True)
    # 输出学生姓名、各科成绩和平均成绩
    print(stu["name"], end=' ')
    for score in sorted_scores[1:]:
        print('{:.2f}'.format(score[1]), end=' ')
    print('{:.2f}'.format(avg))
