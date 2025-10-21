import random

def create_deck():
    """
    Creates a standard 52-card deck as a list of strings.
    """
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(f'{rank} of {suit}')
    return deck

def shuffle_deck(deck):
    """
    Shuffles the deck in place using random.shuffle().
    """
    # random.shuffle shuffles the list in-place (modifies the original list)
    random.shuffle(deck)
    print("The deck has been shuffled! 🃏")

def display_deck(deck):
    """
    Prints the cards in the deck, typically showing the first and last few.
    """
    print("\n--- Current Deck (First 5 and Last 5 cards) ---")
    print(deck[:5])
    print("...")
    print(deck[-5:])
    print(f"\nTotal cards: {len(deck)}")

# --- Main Program ---
if name == "main":
    # 1. Create the sorted deck
    my_deck = create_deck()
    print("Deck created in sorted order.")
    # display_deck(my_deck) # Uncomment to see the initial order

    # 2. Shuffle the deck
    shuffle_deck(my_deck)

    # 3. Display the shuffled deck
    display_deck(my_deck)
