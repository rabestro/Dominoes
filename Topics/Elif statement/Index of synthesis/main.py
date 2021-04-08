synthesis_index = float(input())

language_type = "Analytic" if synthesis_index < 2 \
    else "Polysynthetic" if synthesis_index > 3 \
    else "Synthetic"

print(language_type)
