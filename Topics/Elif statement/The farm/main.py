money = int(input())

def buy(name, price, plural=True):
    if price <= money:
        count = money // price
        print(f"{count} {name}{'s' if plural and count > 1 else''}")
        return True
    else:
        return False


if not (buy('sheep', 6769, False) or buy('cow', 3848) or buy('pig', 1296) 
        or buy('goat', 678) or buy('chicken', 23)):
    print("None")
