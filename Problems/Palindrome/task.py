word = input()
word_len = len(word)
i = 0
is_palindrome = True

while i < word_len / 2 and is_palindrome:
    if word[i] != word[word_len - i - 1]:
        is_palindrome = False
    i = i + 1

if is_palindrome:
    print('Palindrome')
else:
    print('Not palindrome')
