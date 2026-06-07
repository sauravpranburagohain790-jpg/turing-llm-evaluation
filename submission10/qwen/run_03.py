import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def build_sparse_table(arr):
    n = len(arr)
    if n == 0:
        return None, 0
    k = int(math.log2(n)) + 1
    st = [[0] * k for _ in range(n)]
    for i in range(n):
        st[i][0] = arr[i]
    j = 1
    while (1 << j) <= n:
        i = 0
        while i + (1 << j) - 1 < n:
            st[i][j] = max(st[i][j-1], st[i + (1 << (j-1))][j-1])
            i += 1
        j += 1
    return st, k

def query_max(st, left, right):
    if left >= right:
        return 0
    if left == right - 1:
        return st[left][0]
    length = right - left
    j = int(math.log2(length))
    return max(st[left][j], st[right - (1 << j)][j])

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i+1] = prefix[i] + A[i]

    def get_sum(i, j):
        return prefix[j] - prefix[i]

    dp = [-1] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):
        for j in range(i):
            if dp[j] == -1:
                continue
            length = i - j
            total = get_sum(j, i)
            if total % K != 0:
                continue
            if gcd(length, K) != 1:
                continue
            m = max(A[j:i])
            if 2 * m <= total:
                continue
            if dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    print(dp[N])

solve()
