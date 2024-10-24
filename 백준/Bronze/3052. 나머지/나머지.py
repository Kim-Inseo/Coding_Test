num_list = [int(input()) for _ in range(10)]

def divide_42(num):
    num %= 42
    return num

num_set = set(map(divide_42, num_list))

print(len(num_set))