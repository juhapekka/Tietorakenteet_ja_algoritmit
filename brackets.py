def count(n, k):
    # TODO
    # Jos n on pariton palautetaan automaattisesti 0
    if n % 2 != 0:
        return 0

    def helper(auki_jalj, kiini_jalj, syv):
        if auki_jalj == 0 and kiini_jalj == 0:
            return 1

        if syv > k or auki_jalj < 0 or kiini_jalj < 0 or kiini_jalj < auki_jalj:
            return 0

        lisaa_auki = helper(auki_jalj - 1, kiini_jalj, syv + 1)
        lisaa_kiini = helper(auki_jalj, kiini_jalj - 1, syv - 1)
        return lisaa_auki + lisaa_kiini

    # Kutsutaan rekursiivista funktiota n/2 avaavalla ja n/2 sulkevalla sululla. aloitussyvyys 0
    return helper(n // 2, n // 2, 0)

if __name__ == "__main__":
    print(count(6, 1)) # 1
    print(count(6, 2)) # 4
    print(count(6, 3)) # 5
    print(count(9, 1)) # 0
    print(count(16, 4)) # 1094
