def create(t):
    sums = [0]

    for num in t:
        new_sums = [s + num for s in sums]
        sums.extend(new_sums)

    return sorted(sums)

if __name__ == "__main__":
    print(create([1, 2, 3])) # [0, 1, 2, 3, 3, 4, 5, 6]
    print(create([42, 1337])) # [0, 42, 1337, 1379]
    print(create([1, 1, 1])) # [0, 1, 1, 1, 2, 2, 2, 3]
    print(create([5])) # [0, 5]