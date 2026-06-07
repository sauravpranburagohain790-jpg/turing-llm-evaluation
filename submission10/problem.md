# The Harmonic Symphony Partitions

## Story

A maestro is composing a symphony of **N** sequential notes. Each note has an acoustic
frequency, given by an array `A`. The maestro wants to divide the entire symphony into as
many **Harmonic Movements** as possible by placing pauses between certain notes. Each
movement is a contiguous block of notes, and every note must belong to exactly one
movement (the movements together tile the whole symphony in order).

A movement is **Harmonic** if and only if it satisfies **all three** rules:

- **Resonance.** The sum of the frequencies of the notes in the movement is a multiple of
  a given resonance factor **K**.
- **Tempo coprimality.** The number of notes in the movement (its length **L**) is
  strictly coprime to K, i.e. `gcd(L, K) = 1`.
- **Acoustic dominance.** The single loudest note in the movement must be strictly louder
  than all the other notes of that movement combined. That is, if `m` is the maximum
  frequency in the movement and `S` is the movement's total frequency sum, then
  `m > S - m` (equivalently `2·m > S`).

Determine the **maximum number of Harmonic Movements** the symphony can be partitioned
into. If it is impossible to partition the entire symphony into valid Harmonic Movements,
output **-1**.

---

## Input Format

```
N K
A[1] A[2] ... A[N]
```

## Output Format

A single integer: the maximum number of Harmonic Movements, or -1 if no valid partition
of the whole symphony exists.

---

## Constraints

| Parameter | Bound |
|-----------|-------|
| N | 1 ≤ N ≤ 100000 |
| K | 2 ≤ K ≤ 50 |
| A[i] | 1 ≤ A[i] ≤ 10⁹ |

---

## Examples

### Example 1
```
Input:
2 2
4 4

Output:
2
```
**Explanation:** Cut into [4] and [4]. Each has sum 4 (multiple of 2), length 1
(gcd(1,2)=1), and a single note that trivially dominates (2·4 > 4). Two movements.

### Example 2
```
Input:
4 3
3 7 8 9

Output:
3
```
**Explanation:** [3] (sum 3, len 1, 2·3>3); [7,8] (sum 15, multiple of 3, len 2 with
gcd(2,3)=1, and 2·8>15); [9] (sum 9, len 1, 2·9>9). Three movements.

### Example 3
```
Input:
4 2
2 7 11 4

Output:
2
```
**Explanation:** One optimal partition is [2,7,11] and [4]. The first has sum 20 (multiple
of 2), length 3 (gcd(3,2)=1), and max 11 with 2·11 = 22 > 20. The second is a single note.
Two movements.

### Example 4
```
Input:
7 2
12 10 2 10 4 1 1

Output:
5
```
**Explanation:** [12], [10], [2], [10], [4,1,1]. Each single note dominates trivially; the
last block has sum 6 (multiple of 2), length 3 (gcd(3,2)=1), and max 4 with 2·4 = 8 > 6.
Five movements.

### Example 5
```
Input:
6 2
2 4 2 11 5 6

Output:
4
```
**Explanation:** [2], [4], [2,11,5], [6]. The third block has sum 18 (multiple of 2),
length 3 (gcd(3,2)=1), and max 11 with 2·11 = 22 > 18. Four movements.
