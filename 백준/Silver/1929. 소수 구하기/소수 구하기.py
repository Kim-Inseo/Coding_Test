import sys
import math

def is_prime(num):
    if num == 1:
        return 0
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return 0
        
    print(num)
    return 1

m, n = map(int, sys.stdin.readline().rstrip().split())

num_list = []

for i in range(m, n+1):
    num_list.append(i)

prime_list = list(map(is_prime, num_list))