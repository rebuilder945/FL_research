def main():
    num = eval(input())
    calculate_e(num)
double calculate_e(int n) {
  double e = 1.0;
  for (int i = 1; i <= n; i++) {
    e += 1.0 / factorial(i);
  }
  return e;

main()


