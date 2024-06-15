def main():
    stra = input()
    lista= list(stra)
    print("".join(x for x in replece_stars(lista)))

def replace_stars( str_list):  # 将所有*号移动到数组的左侧
    j = len(str_list) - 1
    for i in range(len(str_list) - 1, -1, -1):
        if str_list[i] != '*':
            str_list[j],str_list[i]=str_list[i],str_list[j]
            j -= 1
    return str_list

main()

