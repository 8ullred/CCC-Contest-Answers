players = []
scores = []
above40 = 0
for x in range(int(input())):
    players.append([int(input()), int(input())])
for x in players:
    scores.append((5*x[0]) - (3*x[1]))
for x in scores:
    if x > 40:
        above40 += 1
print(str(len(scores)) + "+") if all(x > 40 for x in scores) else print(above40)
# Code by 8ullred on 02/16/2022
