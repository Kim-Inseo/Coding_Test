import math

def is_prime(num):
    if num == 1:
        return 0
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return 0
    
    return 1

N = int(input())

num_list = list(map(int, input().split()))

prime_list = list(map(is_prime, num_list))

print(sum(prime_list))