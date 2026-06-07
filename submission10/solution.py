import sys
from math import gcd

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    N = int(data[idx]); idx += 1
    K = int(data[idx]); idx += 1
    A = [int(data[idx + i]) for i in range(N)]

    NEG = float('-inf')

    # A movement (contiguous block) is valid iff:
    #   (1) its sum is divisible by K,
    #   (2) gcd(length, K) == 1,
    #   (3) 2 * max(block) > sum(block)   ("the dominant note exceeds all others combined").
    #
    # Rule (3) makes the prefix-sum-mod-K speedup inapplicable, because the max of a block
    # changes as the block grows. The key structural fact is that the number of blocks
    # satisfying rule (3) is near-linear: O(N log V). For a block dominated by A[p], the sum
    # of the OTHER elements must be < A[p], which bounds how far the block can extend.
    #
    # We enumerate every dominant block exactly once by attributing it to the position p of its
    # maximum. Using a monotonic stack we find, for each p, the maximal window
    # (prevGE[p], nextG[p]) in which A[p] is the (strict, with a tie-break) maximum. Within that
    # window we expand left and right, stopping as soon as the sum reaches 2*A[p] (rule 3 fails
    # and can never recover because all values are >= 1). Each valid dominant block that also
    # satisfies rules (1) and (2) becomes an edge l -> r+1 in a DP that maximizes the number of
    # blocks tiling the whole array.

    if N == 0:
        print(0)
        return

    # prevGE[p]: nearest index to the left with A >= A[p]; nextG[p]: nearest right with A > A[p].
    # This pairing attributes each block to a unique maximum position.
    prevGE = [-1] * N
    st = []
    for p in range(N):
        while st and A[st[-1]] < A[p]:
            st.pop()
        prevGE[p] = st[-1] if st else -1
        st.append(p)
    nextG = [N] * N
    st = []
    for p in range(N - 1, -1, -1):
        while st and A[st[-1]] <= A[p]:
            st.pop()
        nextG[p] = st[-1] if st else N
        st.append(p)

    pre = [0] * (N + 1)
    for i in range(N):
        pre[i + 1] = pre[i] + A[i]

    # Collect valid blocks as edges grouped by start index.
    edges_from = [[] for _ in range(N)]  # edges_from[l] = list of end-exclusive indices r+1
    for p in range(N):
        Lb = prevGE[p] + 1
        Rb = nextG[p] - 1
        Ap = A[p]
        two_Ap = 2 * Ap
        for l in range(p, Lb - 1, -1):
            base = pre[l]
            for r in range(p, Rb + 1):
                s = pre[r + 1] - base
                if two_Ap > s:
                    L = r - l + 1
                    if s % K == 0 and gcd(L, K) == 1:
                        edges_from[l].append(r + 1)
                else:
                    break  # all values >= 1, so the sum only grows; rule (3) cannot recover

    dp = [NEG] * (N + 1)
    dp[0] = 0
    for l in range(N):
        if dp[l] == NEG:
            continue
        dl1 = dp[l] + 1
        for e in edges_from[l]:
            if dl1 > dp[e]:
                dp[e] = dl1

    print(dp[N] if dp[N] != NEG else -1)

if __name__ == '__main__':
    solve()
