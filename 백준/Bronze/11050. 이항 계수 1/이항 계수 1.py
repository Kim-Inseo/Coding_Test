n, r = map(int, input().split())

def factorial(num):
    if num == 0:
        return 1
        
    return factorial(num-1) * num

print(factorial(n) // (factorial(n-r) * factorial(r)))