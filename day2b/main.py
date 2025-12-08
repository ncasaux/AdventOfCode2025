import aocd

f = aocd.get_data(day=2, year=2025)
total = 0
ids = []

ranges = [r.strip() for r in f.split(",")]
for r in ranges:
    p = r.index("-")
    mini, maxi = int(r[:r.index("-")]), int(r[r.index("-") + 1:])

    for i in range(mini, maxi + 1):
        half_size = len(str(i)) // 2
        for chunk_size in range(1, half_size + 1):
            chunk_qty = len(str(i)) // chunk_size
            s = [str(i)[k * chunk_size:k * chunk_size + chunk_size] for k in range(0 , chunk_qty)]
            if len(set(s)) == 1 and ''.join(s)==str(i) and i not in ids:
                total += int(i)
                ids.append(i)

print(f"sum: {total}")
