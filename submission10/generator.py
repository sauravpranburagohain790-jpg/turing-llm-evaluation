import sys, random
from math import gcd

def gen(mode, n, K, seed=0):
    random.seed(seed)
    if mode == "trap":
        # mix of single dominant notes and balanced runs that violate dominance, so that
        # ignoring the dominance rule over-counts and greedy strands the suffix.
        A=[]
        while len(A)<n:
            if random.random()<0.5:
                A.append(random.randint(1,9))            # small, balanced -> tends to break dominance
            else:
                A.append(random.choice([8,9,10,11,12]))  # potential dominant note
        A=A[:n]
    elif mode == "max":
        A=[random.randint(1,10**9) for _ in range(n)]
    elif mode == "powers":
        A=[min(10**9, 2**(i%30)) for i in range(n)]      # worst case for segment count
    elif mode == "single_dominant":
        # every element its own movement: divisible-by-K values, each trivially dominant
        A=[K*random.randint(1,5) for _ in range(n)]
    else:
        raise ValueError(mode)
    return f"{len(A)} {K}\n"+" ".join(map(str,A))+"\n"

if __name__=="__main__":
    mode=sys.argv[1] if len(sys.argv)>1 else "trap"
    n=int(sys.argv[2]) if len(sys.argv)>2 else 5000
    K=int(sys.argv[3]) if len(sys.argv)>3 else 3
    seed=int(sys.argv[4]) if len(sys.argv)>4 else 0
    sys.stdout.write(gen(mode,n,K,seed))
