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

print('Stock pieces:', stock_pieces)
print('Computer pieces:', computer_pieces)
print('Player pieces:', player_pieces)
print('Domino snake:', domino_snake)
print('Status:', 'player' if len(computer_pieces) == 6 else 'computer')
