from Cards.Card import Card, Rank

# TODO (TASK 3): Implement a function that evaluates a player's poker hand.
#   Loop through all cards in the given 'hand' list and collect their ranks and suits.
#   Use a dictionary to count how many times each rank appears to detect pairs, three of a kind, or four of a kind.
#   Sort these counts from largest to smallest. Use another dictionary to count how many times each suit appears to check
#   for a flush (5 or more cards of the same suit). Remove duplicate ranks and sort them to detect a
#   straight (5 cards in a row). Remember that the Ace (rank 14) can also count as 1 when checking for a straight.
#   If both a straight and a flush occur in the same suit, return "Straight Flush". Otherwise, use the rank counts
#   and flags to determine if the hand is: "Four of a Kind", "Full House", "Flush", "Straight", "Three of a Kind",
#   "Two Pair", "One Pair", or "High Card". Return a string with the correct hand type at the end.
def evaluate_hand(hand: list[Card]):
    ranks = []
    suits = []

    for card in hand:
        ranks.append(card.rank.value)
        suits.append(card.suit)

    rank_counts = {}
    for rank in ranks:
        rank_counts[rank] = rank_counts.get(rank, 0) + 1

    sorted_counts = sorted(rank_counts.values(), reverse=True)

    suit_counts = {}
    for suit in suits:
        suit_counts[suit] = suit_counts.get(suit, 0) + 1

    is_flush = any(count >= 5 for count in suit_counts.values())

    unique_ranks = sorted(set(ranks))
    is_straight = False

    if len(unique_ranks) >= 5:
        for i in range(len(unique_ranks) - 4):
            if unique_ranks[i + 4] - unique_ranks[i] == 4:
                is_straight = True
                break

    if 14 in unique_ranks and not is_straight:
        if all(rank in unique_ranks for rank in [2, 3, 4, 5]):
            is_straight = True

    if is_straight and is_flush:
        return "Straight Flush"
    elif sorted_counts[0] == 4:
        return "Four of a Kind"
    elif sorted_counts[0] == 3 and sorted_counts[1] == 2:
        return "Full House"
    elif is_flush:
        return "Flush"
    elif is_straight:
        return "Straight"
    elif sorted_counts[0] == 3:
        return "Three of a Kind"
    elif sorted_counts[0] == 2 and sorted_counts[1] == 2:
        return "Two Pair"
    elif sorted_counts[0] == 2:
        return "One Pair"
    else:
        return "High Card"