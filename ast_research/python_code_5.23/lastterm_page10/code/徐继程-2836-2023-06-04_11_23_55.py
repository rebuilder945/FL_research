def main():
    stra = input()
    lista= list(stra)
    print(replace-stars(lista))

def replace_stars( str_list):  # 将所有*号移动到数组的左侧
    j = len(str_list) - 1
    for i in range(len(str_list) - 1, -1, -1):
        if str_list[i] != '*':
            str-list[i],str-list[j]=str-list[j],str-list[i]
            j -= 1
    return str_list

main()

