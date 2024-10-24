N = int(input())

word_list = []
word_len = [[] for _ in range(51)]
final_list = []

for i in range(N):
    word_list.append(input())
    
word_list = list(set(word_list))

for word in word_list:
    word_len[len(word)].append(word)
    
for sub_list in word_len:
    sub_list.sort()
    final_list += sub_list
    
for word in final_list:
    print(word)