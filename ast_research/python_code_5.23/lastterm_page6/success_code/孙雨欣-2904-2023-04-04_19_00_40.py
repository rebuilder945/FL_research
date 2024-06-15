def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    b=a
    all=0
    for i in range(a):
        all=all+b
        b=b*10+a
    print(all)
main()

