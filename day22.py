count = 0

def get_decks(s):
    splits = s.split('\nPlayer 2:\n')
    splits[0] = splits[0][len('Player 1:\n'):]
    for i in splits[0].split('\n'):
        print(i)
    deck1 = [int(i) for i in splits[0].split('\n') if i.isdigit()]
    deck2 = [int(i) for i in splits[1].split('\n') if i.isdigit()]
    print(deck1, deck2)
    return deck1, deck2

def get_score(deck):
    score = 0
    for i, item in enumerate(list(reversed(deck)), 1):
        print(i, item)
        score += item*i
    return score



def play_recursive_combat(deck1, deck2):
    history = set()

    round = 1
    while deck1 and deck2:
        gamestate = (tuple(deck1), tuple(deck2))
        if gamestate in history:
            print('repeata', gamestate)
            return 'p1', deck1
        else:
            history.add(gamestate)

        print('round %d ' % round, deck1, deck2, deck1[0], deck2[0])
        card1, card2 = deck1.pop(0), deck2.pop(0)

        sub_winner = None
        print(card1, len(deck1), card2, len(deck2))
        if card1 < len(deck1)+1 and card2 < len(deck2)+1:
            print('NEW GAME')
            sub_winner = play_recursive_combat(deck1.copy()[:card1], deck2.copy()[:card2])
            if sub_winner[0] == 'p1':
                deck1.append(card1)
                deck1.append(card2)
            else:
                deck2.append(card2)
                deck2.append(card1)
        else:
            if card1 > card2 or sub_winner == 'p1':
                deck1.append(card1)
                deck1.append(card2)
            else:
                deck2.append(card2)
                deck2.append(card1)
        round+=1

    # print('fuck egg nog', deck1, deck2)
    if deck1:
        return 'p1', deck1
    else:
        return 'p2', deck2



get_score([3, 2, 10, 6, 8, 5, 9, 4, 7, 1])
print('fuck')

with open('input.txt', 'r') as f:
    l = []

    lines = '''Player 1:
43
19

Player 2:
2
29
14'''

    # lines = f.readlines() # comment out this line to run above test case
    #
    # lines = [line[:-1] if line[-1] == '\n' else line for line in lines]
    #
    # for line in lines:
    #     pass

    deck1, deck2 = get_decks(f.read())
    # deck1, deck2 = get_decks(lines)

    score1 = score2 = 0

    game = play_recursive_combat(deck1, deck2)
    print('WTF', get_score(game[1]))




    print('Count:', count)

# List of Wrong Answers:
# 32377
# 32665