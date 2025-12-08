import aocd

f = aocd.get_data(day=2, year=2025)
total = 0

ranges = [r.strip() for r in f.split(",")]
for r in ranges:
    p = r.index("-")
    mini, maxi = int(r[:r.index("-")]), int(r[r.index("-") + 1:])

    for i in range(mini, maxi + 1):
        if len(str(i)) % 2 == 1: continue
        half_size = len(str(i)) // 2
        left = str(i).zfill(2 * half_size)[half_size:]
        right = str(i).zfill(2 * half_size)[:half_size]
        if left == right:
            total += int(i)

print(f"sum: {total}")
