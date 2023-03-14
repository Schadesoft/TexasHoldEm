#Texas Hold'em Game in Python
This is a Python implementation of the popular poker game Texas Hold'em. The game is played with a standard deck of 52 cards, and each player is dealt two private "hole" cards and five shared "community" cards. The objective of the game is to make the best possible five-card hand using any combination of the player's hole cards and the community cards.

Requirements
This game requires Python 3 to be installed on your system. The game also uses the random module for shuffling the deck of cards.

Running the Game
To run the game, simply execute the texas_holdem.py file in your Python environment. The game will prompt you to enter the number of players, the starting chip count for each player, and the size of the small and big blinds. The game will then start, and you will be prompted to take your turn when it is your move.

Game Mechanics
Gameplay
The game starts with each player being dealt two hole cards face down, followed by a round of betting. Then, three community cards are dealt face up in the middle of the table, followed by another round of betting. This is repeated twice more, with a fourth and fifth community card being dealt and a round of betting following each. At the end of the final betting round, the players reveal their hole cards, and the player with the best five-card hand using any combination of their hole cards and the community cards wins the pot.

Betting
The game uses a fixed-limit betting structure, meaning that there is a fixed amount that players can bet and raise by. The game starts with the player to the left of the dealer posting the small blind, and the player to their left posting the big blind. The small blind is typically half the size of the big blind.

The betting rounds proceed in a clockwise order, starting with the player to the left of the big blind. Each player has the option to call the current bet, raise the current bet, or fold their hand. If a player raises, the next player must call the raise, raise again, or fold. This continues until all remaining players have either called the final bet or folded.

Evaluating Hands
The game uses standard poker hand rankings to determine the winner. The possible hand rankings, from highest to lowest, are:

Straight flush: Five cards of sequential rank, all in the same suit.
Four of a kind: Four cards of the same rank.
Full house: Three cards of one rank and two cards of another rank.
Flush: Five cards of the same suit.
Straight: Five cards of sequential rank, not all in the same suit.
Three of a kind: Three cards of the same rank.
Two pairs: Two cards of one rank, two cards of another rank, and one card of a third rank.
Pair: Two cards of the same rank.
High card: A hand with no other ranking, determined by the highest card in the hand.
If two or more players have hands of the same rank, the tie is broken by comparing the relevant card indices in the hands, with higher indices representing stronger cards.
