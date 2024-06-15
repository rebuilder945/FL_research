def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    list=[]
    for x in range(a):
        c=int(str(a)*(x+1))
        list.append(c)
    print(sum(list))
main()

