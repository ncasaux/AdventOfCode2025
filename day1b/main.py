import aocd

f = aocd.get_data(day=1, year=2025)

position = 50
hits = 0

instructions = f.splitlines()

for i in instructions:
    hitTurns = int(i[1:]) // 100
    hits += hitTurns

    if i[0] == "L":
        newPosition = (position - int(i[1:])) % 100
        if newPosition > position != 0 or newPosition == 0:
            hits += 1
        position = newPosition
    else:
        newPosition = (position + int(i[1:])) % 100
        if newPosition < position:
            hits += 1
        position = newPosition

print(f"hits: {hits}")
