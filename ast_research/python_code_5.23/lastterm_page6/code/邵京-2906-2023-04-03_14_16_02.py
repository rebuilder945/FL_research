def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(a):
    i=0
    d=0
    while i<a:
    i=(i+2)*2
    d+=1
    print(d)    
main()


