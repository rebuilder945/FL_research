def main():
    input_str = input()
    num_list = list(map(int, input_str.split(',')))

    input_str = input()
    n, m = map(int, input_str.split(','))

    if 0 <= n < len(num_list):
        num_list.extend([num_list[n]] * m)
    else:
        print("error")
        return

    print(num_list)

if __name__ == "__main__":
    main()

