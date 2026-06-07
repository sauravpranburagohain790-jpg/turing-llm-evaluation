# Turing LLM Evaluation — Harmonic Symphony Partitions

A complete competitive programming problem designed to evaluate and expose failure modes in frontier LLMs (specifically Qwen3-235B-A22B-2507 with thinking disabled).

## Problem Summary

**The Harmonic Symphony Partitions** — partition an array into the maximum number of contiguous movements where each movement satisfies three rules:
1. **Resonance:** sum divisible by K
2. **Tempo coprimality:** length coprime to K
3. **Acoustic dominance:** max element strictly exceeds the sum of all other elements (2·max > sum)

Output -1 if no valid full partition exists.

## Why This Problem Is LLM-Proof

Three independent failure layers, each targeting a different model weakness:

| Attempt | What Qwen writes | Why it fails |
|---------|-----------------|--------------|
| 1 | Greedy (cut at first valid prefix) | Wrong Answer — coprimality breaks optimal substructure |
| 2 | Naive O(N²) DP | Time Limit Exceeded at N = 100,000 |
| 3 | Prefix-sum-mod-K O(N·K) trick | Wrong Answer — acoustic dominance cannot be encoded as a prefix residue |

The standard "divisible by K → store remainders" optimization (one of the most documented CP patterns) is deliberately invalidated by rule 3.

## Correct Solution: O(N log V)

Rule 3 limits the number of valid blocks to **O(N log V)**:
- A block dominated by A[p] can only contain other elements summing to less than A[p]
- Enumerate all dominant blocks via a **monotonic stack** (each attributed to its unique maximum position)
- Filter by rules 1 and 2, then run a **partition DP** over O(N log V) blocks

This insight — that the dominance rule bounds segment count — is non-templated and unlikely to be assembled in a single pass by a non-thinking model.

## Repository Structure

```
submission10/
├── problem.md          # Full problem statement
├── solution.py         # Correct O(N log V) solution (monotonic stack + DP)
├── solution_bf.py      # O(N²) brute force for validation
├── solution.md         # Algorithm explanation and correctness proof
├── idea.md             # Design rationale and rejected variants
├── generator.py        # Adversarial test case generator
├── requirements.json   # Time/space limits
├── test_cases/         # 6 test cases (lures + WA traps + TLE trap)
└── qwen/
    ├── conversations.md    # 4 Qwen failure attempts with share links
    ├── run_01.py           # Qwen attempt 1: greedy
    ├── run_02.py           # Qwen attempt 2: naive O(N²) DP
    └── run_03.py           # Qwen attempt 3: prefix-sum trick (ignores dominance)
```

## Verified Results

- `solution.py` matches `solution_bf.py` on 8,000+ random test cases — zero mismatches
- All 3 Qwen attempts pass the small sample tests and fail the large case (TLE or WA)
- Correct solution runs in **0.27s** at N = 100,000

## About

Built as part of Turing's Python TopCoder Problemsetter Assessment.  
Model tested: **Qwen3-235B-A22B-2507** (thinking disabled / Fast mode)  
Platform: https://chat.qwen.ai
