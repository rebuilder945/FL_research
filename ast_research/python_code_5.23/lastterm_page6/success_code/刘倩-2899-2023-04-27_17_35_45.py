def find_unique_combinations(n, m):
    if n < 0 or m > 9 or n >= m:
        return "illegal input"

    combinations = []
    for i in range(n, m):
        for j in range(n, m):
            if j == i:
                continue
            for k in range(n, m):
                if k == i or k == j:
                    continue
                combinations.append(str(i) + str(j) + str(k))

    if not combinations:
        return "illegal input"

    return ' '.join(combinations)


def main():
    n, m = map(int, input().split())

    print(find_unique_combinations(n, m))


if __name__ == "__main__":
    main()

