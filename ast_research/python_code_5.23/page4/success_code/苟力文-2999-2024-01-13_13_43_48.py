def main():
    input_str = input()
    input_list = [int(x) for x in input_str.strip('[]').split(',')]
    average = sum(input_list) / len(input_list)
    print("{:.2f}".format(average))

if __name__ == "__main__":
    main()

