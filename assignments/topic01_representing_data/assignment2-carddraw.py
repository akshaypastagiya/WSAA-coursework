import requests

# Shuffle a card
shuffle_url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"

response = requests.get(shuffle_url,verify=False)
data = response.json()
# Using Shuffle card get the dack id
dack_id = data['deck_id']

# draw a 5 cards 
draw_url = "https://deckofcardsapi.com/api/deck/"+dack_id+"/draw/?count=5"
response = requests.get(draw_url,verify=False)
data = response.json()

# Use this rank to convert card to integer value
rank_map = {"ACE": 14, "KING": 13, "QUEEN": 12, "JACK": 11}
# get cards data
cards = data.get("cards", [])

values = []
ranks = []
suits = []

# Get Suit and card value from the card data
for card in cards:
    rank = card.get('value')
    suit = card.get('suit')

    # Convert to numeric value    
    mapped = rank_map.get(rank)
    if mapped is not None:
        value = mapped
    else:
        # Numeric ranks "2".."10"
        value = int(rank)

    ranks.append(rank)
    values.append(value)
    suits.append(suit)    
    
print(f"my card are {ranks} of {suits}")

# i have used copilot to get evelue the card sequence for responce click here https://atlantictu-my.sharepoint.com/:w:/r/personal/g00473015_atu_ie/Documents/import%20requests%20Shuffle%20a%20cardshuffle_url.docx?d=w997cee6a489c4c368772a769557d6c50&csf=1&web=1&e=l0qzPc9+

# Hand evaluation helpers
def is_flush(suits_list):
    return len(set(suits_list)) == 1

def is_straight(values_list):
    """
    Five-card straight check.
    Handles Ace high (14) and Ace low (A-2-3-4-5) by remapping Ace to 1 for a second pass.
    """
    uniq = sorted(set(values_list))
    if len(uniq) != 5:
        return False
    # Normal straight
    if max(uniq) - min(uniq) == 4:
        return True
    # Ace-low straight: treat 14 as 1
    if 14 in uniq:
        low = sorted(1 if v == 14 else v for v in uniq)
        return max(low) - min(low) == 4
    return False

def count_pairs(values_list):
    counts = Counter(values_list)
    return sum(1 for c in counts.values() if c == 2)

def has_n_of_a_kind(values_list, n):
    counts = Counter(values_list)
    return any(c == n for c in counts.values())

#  Evaluate hand 
flush = is_flush(suits)
straight = is_straight(values)
triple = has_n_of_a_kind(values, 3)
pair = count_pairs(values) >= 1

messages = []
if flush:
    messages.append("Flush! All cards are the same suit 🎉")
if straight:
    messages.append("Straight! Five cards in sequence 🔥")
if triple:
    messages.append("Three of a kind! 🎊")
elif pair:
    messages.append("Nice, you’ve got a pair! 🎉")

if messages:
    for m in messages:
        print(m)
else:
    print("No pair, triple, straight, or flush this time—try again!")
