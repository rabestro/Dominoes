age = int(input())
movie = "Lion King" if age < 17 \
    else "Trainspotting" if age < 26 \
    else "Matrix" if age < 41 \
    else "Pulp Fiction" if age < 61 \
    else "Breakfast at Tiffany's"

print(movie)
