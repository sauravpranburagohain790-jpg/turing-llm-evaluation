import math
from math import gcd

def can_form_harmonic_movement(arr, start, end, K):
    """Check if subarray from start to end (inclusive) forms a valid harmonic movement"""
    subarray = arr[start:end+1]
    length = len(subarray)
    total_sum = sum(subarray)
    max_val = max(subarray)
    if total_sum % K != 0:
        return False
    if gcd(length, K) != 1:
        return False
    if 2 * max_val <= total_sum:
        return False
    return True

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [-1] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):
        for j in range(i):
            if dp[j] != -1:
                if can_form_harmonic_movement(A, j, i - 1, K):
                    if dp[i] == -1:
                        dp[i] = dp[j] + 1
                    else:
                        dp[i] = max(dp[i], dp[j] + 1)
    return dp[N]

result = solve()
print(result)
