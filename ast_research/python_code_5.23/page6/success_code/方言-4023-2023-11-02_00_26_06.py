def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(q):
  i=0
  while q>0:
    p=int(q/2)
    q=q-2-p
    i=i+1
main()


