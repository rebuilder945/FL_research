def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    b=[a]
    c=[]
    for i in range(a):
        c.append(''.join(str(x) for x in b*i))
    print(sum(c))
main()

