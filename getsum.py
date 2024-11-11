def count(n, k, x):
    def helper(start, remaining_k, remaining_sum):

        if remaining_k == 0 and remaining_sum == 0:
            return 1

        if remaining_k == 0 or remaining_sum < 0:
            return 0

        ways = 0
        for i in range(start, n + 1):
            ways += helper(i + 1, remaining_k - 1, remaining_sum - i)
        return ways

    return helper(1, k, x)

if __name__ == "__main__":
    print(count(1, 1, 1)) # 1
    print(count(5, 2, 6)) # 2
    print(count(8, 3, 12)) # 6
    print(count(10, 4, 20)) # 16