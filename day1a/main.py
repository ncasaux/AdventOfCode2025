import aocd

f = aocd.get_data(day=1, year=2025)

position = 50
hits = 0

instructions = f.splitlines()

for i in instructions:
    if i[0] == "L":
        position = (position - int(i[1:])) % 100
    else:
        position = (position + int(i[1:])) % 100
    if position == 0:
        hits += 1

print(f"hits: {hits}")
