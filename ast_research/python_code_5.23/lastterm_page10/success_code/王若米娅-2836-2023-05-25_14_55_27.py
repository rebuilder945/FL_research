def main():
    stra = input()
    lista= list(stra)
    print(replace_stars(lista))

def replace_stars( str_list):  # 将所有*号移动到数组的左侧
    j = len(str_list) - 1
    for i in range(len(str_list) - 1, -1, -1):
        if str_list[i] != '*':
            
            str_list.pop(i)
            c=str_list.pop(i)
            str_list.append(c)
            j -= 1
    return str_list

main()

