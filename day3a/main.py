import aocd

f = aocd.get_data(day=3, year=2025)

banks = f.splitlines()
total = 0

for bank in banks:
    maxTenIndex = 0
    for i in range(1, len(bank) - 1):
        if bank[i] > bank[maxTenIndex]: maxTenIndex = i

    maxUnitIndex = maxTenIndex + 1
    for i in range(maxUnitIndex + 1, len(bank)):
        if bank[i] > bank[maxUnitIndex]: maxUnitIndex = i

    total += int(bank[maxTenIndex]) * 10 + int(bank[maxUnitIndex])

print(f"total: {total}")