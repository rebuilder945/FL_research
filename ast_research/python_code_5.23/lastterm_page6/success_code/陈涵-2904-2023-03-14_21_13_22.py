def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    a=str(a)
    n=[a]
    while len(n)<int(a):
        a=a+a
        n.append(a)
    m=[int(i) for i in range (len(n))]
    print(sum(m))
main()

