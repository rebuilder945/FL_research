def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    a=[]
    while total_count>0:
        if total_count>0:
            total_count=int(total_count-(int(0.5*total_count)+2))
            a.append(total_count)       
        else:
             break
    print(len(a))
main()


