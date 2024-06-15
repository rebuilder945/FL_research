def remove_duplicates(lst):
    # 用字典记录每个元素最后出现的位置
    last_seen = {}
    for i, val in enumerate(lst):
        last_seen[val] = i

    # 保留每个元素最后出现的位置对应的元素
    result = []
    for i, val in enumerate(lst):
        if i == last_seen[val]:
            result.append(val)

    return result
