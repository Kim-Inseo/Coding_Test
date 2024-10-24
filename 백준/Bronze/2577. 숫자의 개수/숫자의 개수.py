a = int(input())
b = int(input())
c = int(input())

mul = a * b * c

num_list = [0 for _ in range(10)]

for num in str(mul):
    num_list[int(num)] += 1
    
for count in num_list:
    print(count)