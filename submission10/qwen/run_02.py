import math
from functools import lru_cache

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i+1] = prefix[i] + A[i]

    def get_sum(i, j):
        return prefix[j] - prefix[i]

    @lru_cache(maxsize=None)
    def is_harmonic(i, j):
        length = j - i
        total = get_sum(i, j)
        if total % K != 0:
            return False
        if gcd(length, K) != 1:
            return False
        m = max(A[i:j])
        if 2 * m <= total:
            return False
        return True

    dp = [-10**9] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):
        for j in range(i):
            if dp[j] >= 0 and is_harmonic(j, i):
                dp[i] = max(dp[i], dp[j] + 1)

    result = dp[N]
    print(result if result >= 0 else -1)

solve()
