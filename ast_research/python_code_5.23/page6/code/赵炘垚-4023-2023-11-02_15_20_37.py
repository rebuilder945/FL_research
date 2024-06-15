def main():
    total_count = int(input())
    calculate_days(total_count)

from math import ceil

def calculate_days(count):
    print(_calculate_days(count))

def _calculate_days(remainingMelons,days-0):
    if remainingMelons <= 0:return days
    else:return _calculate_days(ceil(remainingMelons / 2) - 2,days + 1)

main()


