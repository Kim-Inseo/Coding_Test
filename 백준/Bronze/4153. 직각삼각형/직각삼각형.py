import sys

while True:
    length = list(map(int, sys.stdin.readline().rstrip().split()))

    length.sort()
    a, b, c = length

    if a == 0 and b == 0 and c == 0:
        break
    elif a ** 2 + b ** 2 == c ** 2:
        print('right')
    else:
        print('wrong')