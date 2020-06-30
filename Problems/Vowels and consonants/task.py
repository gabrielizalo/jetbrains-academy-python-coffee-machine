sequence = input()
vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'

for c in sequence:
    if c not in vowels and c not in consonants:
        break

    if c in vowels:
        print('vowel')
    else:
        print('consonant')
