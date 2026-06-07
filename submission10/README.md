# The Harmonic Symphony Partitions (with Acoustic Dominance)

Partition the array into the maximum number of contiguous movements where each movement has
(1) sum divisible by K, (2) length coprime to K, and (3) its max strictly exceeds the sum of
its other elements (2*max > sum). Output -1 if no full partition exists.

## The trap (three layers)
- Greedy -> Wrong Answer: no valid exchange argument; first-valid-prefix strands the suffix.
- Naive O(N^2) DP -> TLE at N = 1e5.
- Prefix-sum-mod-K O(N*K) trick -> Wrong Answer: the standard "divisible by K" remainder-bucket
  speedup cannot represent the dominance rule (a block's max is not a prefix-sum residue), so
  it over-counts. This is the shortcut that solves the dominance-free version; rule (3) breaks it.

## Correct solution: O(N log V)
Rule (3) makes the number of valid (dominant) blocks near-linear: for a block dominated by
A[p], the other elements sum to less than A[p], bounding its extent. Enumerate every dominant
block once via a monotonic stack (attributing each to its maximum position), filter by rules
(1) and (2), and run a DP over these O(N log V) blocks to maximize the count.

## Files
problem.md, solution.md, solution.py (monotonic-stack + DP), solution_bf.py (O(N^2) brute),
generator.py (trap / max / powers / single_dominant), requirements.json,
test_cases/ (1-2 lures, 3-5 break both greedy and the prefix trick, 6 large TLE trap),
qwen/ (3 failed attempts: greedy WA, naive TLE, prefix-trick WA).
