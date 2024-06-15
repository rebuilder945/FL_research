def mix_colors(color1, color2):
    primary_colors = {'red', 'blue', 'yellow'}
    secondary_colors = {
        frozenset(['red', 'blue']): 'purple',
        frozenset(['red', 'yellow']): 'orange',
        frozenset(['blue', 'yellow']): 'green'
    }

    if color1 == color2:
        print("error")
        return

    if color1 in primary_colors and color2 in primary_colors:
        pair = frozenset([color1, color2])
        if pair in secondary_colors:
            print(secondary_colors[pair])
        else:
            print("error")
    else:
        print("error")

def main():
    color1 = input("请输入第一种颜色: ").lower()
    color2 = input("请输入第二种颜色: ").lower()

    mix_colors(color1, color2)

if __name__ == "__main__":
    main()
