def count_foreign(ids):
        count = 0   # 初始化留学生人数为0
        for id in ids:
            if len(id) == 9 and id[0] == 'L':
                count += 1   # 如果是留学生学号，留学生人数加1
        return count

origin=input().split()
print(count_foreign(origin))

