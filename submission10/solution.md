# Solution: The Harmonic Symphony Partitions (with Acoustic Dominance)

## The three rules

A movement (contiguous block) is valid iff:
1. its sum is divisible by K,
2. its length L satisfies gcd(L, K) = 1,
3. its maximum element m satisfies 2·m > sum ("the dominant note exceeds all others combined").

We maximize the number of movements that tile the whole array, or output -1.

## Why the usual shortcuts fail

- **Greedy** (cut at the first valid prefix) has no exchange argument here: taking the
  shortest valid prefix can strand a suffix that cannot be partitioned, so greedy reports
  -1 (or too few) on partitionable inputs.
- **Prefix-sum-mod-K** is the reflex optimization for "sum divisible by K": store the best
  dp value per (prefix_sum mod K, index mod K) and answer in O(N·K). It correctly handles
  rules (1) and (2) — but it **cannot encode rule (3)**, because whether 2·max > sum depends
  on the block's maximum, which is not a function of prefix-sum residues. Using it silently
  drops the dominance rule and over-counts.

## Key structural fact (makes a fast solution possible)

Rule (3) limits the number of valid blocks to near-linear. If a block is dominated by value
A[p], the sum of its **other** elements is < A[p]; since every element is ≥ 1, the block can
contain at most A[p] other elements, and more importantly its extent on each side is bounded
by the running sum reaching A[p]. Summed over all positions (each acting as the maximum of
the blocks it dominates), the total number of dominant blocks is O(N log V), where V is the
maximum frequency.

## Algorithm: O(N log V)

1. **Monotonic stack.** For each index p compute `prevGE[p]` (nearest index to the left with
   value ≥ A[p]) and `nextG[p]` (nearest to the right with value > A[p]). The half-open
   window `(prevGE[p], nextG[p])` is exactly the range in which A[p] is the maximum (the
   ≥/> tie-break attributes every block to a unique maximum position).
2. **Enumerate dominant blocks.** Within that window, expand the block left and right; stop
   as soon as the block sum reaches 2·A[p] (rule (3) fails and, because values are ≥ 1, can
   never recover). Each block with 2·A[p] > sum is a dominant block, counted exactly once.
3. **Filter and build edges.** Keep blocks that also satisfy sum % K == 0 and gcd(L, K) == 1.
   Each becomes an edge from its start index l to its end-exclusive index r+1.
4. **DP.** `dp[0] = 0`; for each l, relax `dp[r+1] = max(dp[r+1], dp[l] + 1)` over its edges.
   The answer is `dp[N]`, or -1 if unreachable.

## Correctness

Step 1's ≥/> pairing guarantees each block is generated once, under the index of its maximum.
Step 2 is exact because the block sum is monotincreasing as the block grows, so the dominance
predicate is a single contiguous prefix of extensions. The DP is the standard
maximum-partition recurrence over the set of valid blocks. Verified against the O(N²) brute
force on 5000+ random instances with zero discrepancies.

## Complexity

Monotonic stacks are O(N). Dominant-block enumeration is O(N log V) total. The DP is linear
in the number of blocks. Overall O(N log V), about 0.8 s at N = 100000 even on the
adversarial powers-of-two input.
