def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(b):
    c=[b]
    for i in range(b):
        c.append(b*i)
    total=sum(c)
    print(total)
main()

