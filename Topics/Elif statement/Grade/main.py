score = 100 * int(input()) / int(input())
print(
    "F" if score < 60 else
    "D" if score < 70 else 
    "C" if score < 80 else
    "B" if score < 90 else
    "A"
)
