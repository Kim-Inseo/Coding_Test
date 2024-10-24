a, b = map(int, input().split())
copy_a, copy_b = a, b

while True:
    if a >= b:
        if a % b == 0:
            gcd = b
            break
        else:
            a %= b
    else:
        if b % a == 0:
            gcd = a
            break
        else:
            b %= a
            
print(gcd)
print(copy_a * copy_b // gcd)       