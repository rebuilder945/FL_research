def generate_permutations(n, m):
    if n >= m:
        print("illegal input")
        return
    
    valid_numbers = [str(i) for i in range(n, m)]

    permutations = [a + b + c for a in valid_numbers for b in valid_numbers if b != a for c in valid_numbers if c != a and c != b]

    result = ' '.join(permutations)
    print(result)

def main():
    try:
        n, m = map(int, input().split())
        generate_permutations(n, m)
    except ValueError:
        print("illegal input")

if __name__ == "__main__":
    main()
