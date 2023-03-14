import random

# Initialize deck
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
deck = [(rank, suit) for suit in suits for rank in ranks]
random.shuffle(deck)

# Initialize players and their starting chips
player1 = {"name": "Player 1", "chips": 100}
player2 = {"name": "Player 2", "chips": 100}
players = [player1, player2]

# Initialize pot
pot = 0

# Deal cards to players
def deal_cards():
    for player in players:
        player["hand"] = [deck.pop(), deck.pop()]

# Print players' hands
def show_hands():
    for player in players:
        print(player["name"] + "'s hand: " + str(player["hand"]))

# Determine winner
def determine_winner():
    player1_score = evaluate_hand(player1["hand"])
    player2_score = evaluate_hand(player2["hand"])
    if player1_score > player2_score:
        print(player1["name"] + " wins!")
        player1["chips"] += pot
    elif player2_score > player1_score:
        print(player2["name"] + " wins!")
        player2["chips"] += pot
    else:
        print("It's a tie!")
        player1["chips"] += pot // 2
        player2["chips"] += pot // 2

# Evaluate hand
def evaluate_hand(hand):
    # Sort hand by rank
    hand = sorted(hand, key=lambda x: ranks.index(x[0]))
    
    # Check for straight flush
    flush_suits = {card[1] for card in hand}
    if len(flush_suits) == 1:
        straight_cards = [ranks.index(card[0]) for card in hand]
        if max(straight_cards) - min(straight_cards) == 4:
            return 8, max(straight_cards)
    
    # Check for four of a kind
    for rank in ranks:
        if hand.count((rank,)) == 4:
            return 7, ranks.index(rank)
    
    # Check for full house
    if hand.count((hand[0][0],)) == 3 and hand.count((hand[-1][0],)) == 2:
        return 6, ranks.index(hand[0][0])
    elif hand.count((hand[0][0],)) == 2 and hand.count((hand[-1][0],)) == 3:
        return 6, ranks.index(hand[-1][0])
    
    # Check for flush
    if len(flush_suits) == 1:
        return 5, [ranks.index(card[0]) for card in hand][::-1]
    
    # Check for straight
    straight_cards = [ranks.index(card[0]) for card in hand]
    if len(set(straight_cards)) == 5 and max(straight_cards) - min(straight_cards) == 4:
        return 4, max(straight_cards)
    elif set(straight_cards) == {0, 1, 2, 3, 12}:
        return 4, 3
    
    # Check for three of a kind
    for rank in ranks:
        if hand.count((rank,)) == 3:
            kickers = [ranks.index(card[0]) for card in hand if card[0] != rank][::-1]
            return 3, ranks.index(rank), kickers
    
    # Check for two pairs
    pairs = []
    for rank in ranks:
        if hand.count((rank,)) == 2:
            pairs.append(rank)
    if len(pairs) == 2:
        kickers = [ranks.index(card[0]) for card in hand if card[0] not in pairs][::-1]
        return 2, ranks.index(pairs[1]), ranks.index(pairs[0]), kickers
    
    # Check for pair
    for rank in ranks:
        if hand.count((rank,)) == 2:
            kickers = [ranks.index(card[0]) for card in hand if card[0] != rank][::-1]
            return 1, ranks.index(rank), kickers
    
    # High card
    return 0, [ranks.index(card[0]) for card in hand][::-1]


# Main game loop
while True:
    # Check if any players have run out of chips
    for player in players:
        if player["chips"] == 0:
            print(player["name"] + " is out of chips!")
            players.remove(player)
    if len(players) == 1:
        print(players[0]["name"] + " wins!")
        break
    
    # Deal cards
    deal_cards()
    
    # Print players' hands
    show_hands()
    
    # Take bets
    for player in players:
        bet = int(input(player["name"] + ", enter your bet: "))
        player["chips"] -= bet
        pot += bet
    
    # Flop
    flop = [deck.pop() for i in range(3)]
    print("Flop: " + str(flop))
    
    # Take bets
    for player in players:
        bet = int(input(player["name"] + ", enter your bet: "))
        player["chips"] -= bet
        pot += bet
    
    # Turn
    turn = deck.pop()
    print("Turn: " + str(turn))
    
    # Take bets
    for player in players:
        bet = int(input(player["name"] + ", enter your bet: "))
        player["chips"] -= bet
        pot += bet
    
    # River
    river = deck.pop()
    print("River: " + str(river))
    
    # Take bets
    for player in players:
        bet = int(input(player["name"] + ", enter your bet: "))
        player["chips"] -= bet
        pot += bet
    
    # Determine winner
    determine_winner()
    
    # Reset pot and players' hands
    pot = 0
    for player in players:
        player["hand"] = []
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)

    # Check if any players have run out of chips
    for player in players:
        if player["chips"] == 0:
            print(player["name"] + " is out of chips!")
            players.remove(player)
    if len(players) == 1:
        print(players[0]["name"] + " wins!")
    break

