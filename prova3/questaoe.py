from math import factorial

n = int(input())
part1 = factorial(n)/n
part2 = factorial(n-1)/(n-1)
output_n = part1 - part2*2


if output_n < 0:
    print(0)
else:
    print(int(output_n))
