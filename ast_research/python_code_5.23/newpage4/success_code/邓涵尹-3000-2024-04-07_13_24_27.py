def is_increasing(lst):
    for i in range(len(lst)-1):
        if lst[i] >= lst[i+1]:  # 应该是严格大于的条件
            return True
    return False

def main():
    a = [1, 2, 3, 99, 100, 6, 7]
    b = [1, 2, 3, 99, 100, 6, 7]
    c = [1, 2, 3, 4, 5, 6, 7]

    result_a = is_increasing(a)
    result_b = is_increasing(b)
    result_c = is_increasing(c)

    print(f'a= {a} {result_a}')
    print(f'b= {b}')
    print(f'c= {c} {result_c}')

if __name__ == "__main__":
    main()

