N = int(input())

coordinate_list = []

for xy in range(N):
    x, y = map(int, input().split())
    coordinate_list.append([x, y])
    
coordinate_list.sort(key=lambda c: (c[0], c[1]))

for coordinate in coordinate_list:
    print(coordinate[0], coordinate[1])