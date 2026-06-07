import sys
from math import gcd

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    N = int(data[idx]); idx += 1
    K = int(data[idx]); idx += 1
    A = [int(data[idx + i]) for i in range(N)]

    NEG = float('-inf')
    pre = [0] * (N + 1)
    for i in range(N):
        pre[i + 1] = pre[i] + A[i]

    dp = [NEG] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):
        mx = 0
        for j in range(i - 1, -1, -1):
            if A[j] > mx:
                mx = A[j]
            if dp[j] == NEG:
                continue
            s = pre[i] - pre[j]
            L = i - j
            if s % K == 0 and gcd(L, K) == 1 and 2 * mx > s:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
    print(dp[N] if dp[N] != NEG else -1)

if __name__ == '__main__':
    solve()
