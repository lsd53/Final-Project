#! /usr/bin/env python
import sys

# print "Player 1 - Enter A Number!"
# x1 = raw_input()
# print "Player 2 - Enter A Number!"
# x2 = raw_input()

# gameover = False
# winner = False

# while (not gameover):
# 	print "Player 1, enter a guess!"
# 	guess = raw_input()
# 	if guess == x2:
# 		gameover = True
# 		winner = 1
# 	else:
# 		(b,c) = giveHint(guess, x2)
# 	print "Player 2, enter a guess!"
# 	guess = raw_input()
# 	if guess == x1:
# 		gameover = True
# 		winner = 2
# 	else:
# 		(b,c) = giveHint(guess, x1)

# print "Player " + str(winner) + ", you win!"


def giveHint(guess, answer):
	glist = list(str(guess))
	alist = list(str(answer))
	cows = 0
	bulls = 0
	for i in range(len(glist)):
		if glist[i] == alist[i]:
			bulls += 1
		elif glist[i] in alist:
			cows += 1
	return (bulls, cows)
