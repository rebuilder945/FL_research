def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    b=[a]
    c=''
    d=str(a)
    for i in range(a):
        c+=d
        b.append(int(c))
    print(sum(b))
main()

