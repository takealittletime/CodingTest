dwarfs = [int(input()) for _ in range(9)]

dwarfs_total = sum(dwarfs)

for i in range(9):
    for j in range(i+1, 9):
        if (dwarfs_total - (dwarfs[i]+dwarfs[j])) == 100:
            fake_dwarfs = [dwarfs[i], dwarfs[j]]
            dwarfs = [d for d in dwarfs if d not in fake_dwarfs]

            dwarfs.sort()
            for dwarf in dwarfs:
                print(dwarf)
            exit()