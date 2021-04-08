index = float(input())
system_type = "Analytic" if index < 2 else "Polysynthetic" if index > 3 else "Synthetic"

print(system_type)
