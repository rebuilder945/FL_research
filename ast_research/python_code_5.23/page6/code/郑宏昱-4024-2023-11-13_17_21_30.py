def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    for i in range(a):
    lst=[]
        b=int(str(a)*(i+1))
        lst.append(b)
    print(sum(lst))
main()

