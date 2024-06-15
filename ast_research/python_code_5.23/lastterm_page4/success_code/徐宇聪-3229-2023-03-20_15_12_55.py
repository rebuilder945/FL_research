def find_unique(lst):
    count = {}
    for num in lst:
        count[num] = count.get(num, 0) + 1
    return [num for num in lst if count[num] == 1]
def main():
    lst = eval(input())
    unique_lst = find_unique(lst)
    if unique_lst:
        unique_lst.sort()
        print(",".join(map(str, unique_lst)))
    else:
        print(False)
if __name__ == '__main__':
    main()
