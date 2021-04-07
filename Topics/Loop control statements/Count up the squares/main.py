square_sum = 0
number_sum = 0

while True:
    number = int(input())
    number_sum += number
    square_sum += number * number
    if number_sum == 0:
        break

print(square_sum)
