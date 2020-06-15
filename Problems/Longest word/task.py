word1 = input()
word2 = input()

# How many letters does the longest word contain?
len_word1 = len(word1)
len_word2 = len(word2)
max_len = 0

if len_word1 >= len_word2:
    max_len = len_word1
else:
    max_len = len_word2

print(max_len)
