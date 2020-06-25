scores = input().split()
wins = 0
loses = 0

for score in scores:
    if score == 'C':
        wins += 1
    else:
        loses += 1
    if loses == 3:
        break

if loses == 3:
    print("Game over")
else:
    print("You won")
print(wins)
