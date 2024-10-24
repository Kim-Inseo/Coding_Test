S = input()

alphabet = 'abcdefghijklmnopqrstuvwxyz'

find_list = [S.find(letter) for letter in alphabet]

for find_result in find_list:
    print(find_result, end=' ')