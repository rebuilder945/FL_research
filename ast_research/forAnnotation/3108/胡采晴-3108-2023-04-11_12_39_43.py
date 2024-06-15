def count_each_char(str):
    dict = {}
    for i in str:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    return dict
 
if __name__ == "__main__":
    res = count_each_char("abdefdcsdf")
    print(res)
