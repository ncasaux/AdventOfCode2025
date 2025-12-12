import aocd

f = aocd.get_data(day=3, year=2025)

banks = f.splitlines()
total = 0
positions = [None] * 12

for bank in banks:
    usedIndex = -1
    nbr = ""
    for p in range(12):
        usedIndex += 1
        positions[p] = usedIndex

        for i in range(usedIndex, len(bank) - 11 + p):
            if bank[i] > bank[positions[p]]:
                positions[p] = i
                usedIndex = i

        nbr += bank[positions[p]]
    total += int(nbr)

print(f"total: {total}")
