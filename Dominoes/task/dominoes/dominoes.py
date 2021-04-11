import random


def generate_stock():
    return [[a, b] for a in range(7) for b in range(a, 7)]


stock_pieces = generate_stock()
random.shuffle(stock_pieces)

player_pieces = stock_pieces[0:7]
computer_pieces = stock_pieces[7:14]
stock_pieces = stock_pieces[14:]
domino_snake = []

for i in range(6, -1, -1):
    piece = [i, i]
    if piece in computer_pieces or piece in player_pieces:
        domino_snake.append(piece)
        if piece in computer_pieces:
            computer_pieces.remove(piece)
        else:
            player_pieces.remove(piece)
        break

# print('Player pieces:', player_pieces)
is_player_turn = len(computer_pieces) == 6
# print('Status:', 'player' if len(computer_pieces) == 6 else 'computer')
your_pieces = '\n'.join(f"{i}: {player_pieces[i - 1]}" for i in range(1, len(player_pieces) + 1))

print(f"""======================================================================
Stock size: {len(stock_pieces)}
Computer pieces: {len(computer_pieces)}

{domino_snake[0]}

Your pieces:
{your_pieces}

Status: {"It's your turn to make a move. Enter your command." if is_player_turn
else "Computer is about to make a move. Press Enter to continue..."}
""")
