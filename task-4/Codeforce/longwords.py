n = int(input())
list_word = []
for i in range(n):
    words = input()
    list_word.append(words)

for i in range(len(list_word)): 
    if len(list_word[i]) > 10:
        words = list_word[i]
        print(words[0] + str(len(words[1:-1])) + words[-1])
    else:
        print(list_word[i])