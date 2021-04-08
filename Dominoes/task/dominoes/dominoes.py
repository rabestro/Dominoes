# Write your code here
def generate_stock():
    stock = []
    for i in range(7):
        for j in range(0, i + 1):
            stock.append([j, i])
    return stock


stock = generate_stock()
print(stock)
