def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    for x in range(a):
        b=int(str(a)*(x+1))
        lst=[]
        lst.append(b)
    print(sum(lst))
main()

