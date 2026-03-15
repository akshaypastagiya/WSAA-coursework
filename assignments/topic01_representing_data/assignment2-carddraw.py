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
rank_map = {"ACE": 14, "KING": 13, "QUEEN": 12, "JACK": 11}
rank = []
for card in data.get('cards',[]):
    value = card.get('value')
    suit = card.get('suit')
    if value == 'ACE':
        valueint = 14
    elif value == 'KING':
        valueint = 13
    elif value == 'QUEEN':
        valueint = 13
    elif value == 'JACK':
        valueint = 11
    else:
        valueint = int(value)
    rank.append(valueint)
    print(f"my card is {value} of {suit}")
print(rank)