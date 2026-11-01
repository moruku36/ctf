"""Predict the next Model E1337 code from two consecutive leaked codes.

The 32-bit seed-to-output mapping is affine over GF(2).  Build its 52 output
equations from the zero seed and each one-bit seed, then solve for the seed.
"""

import sys

MASK = (1 << 64) - 1


def setup(seed):
    state = 0
    for _ in range(16):
        cur = seed & 3
        seed >>= 2
        state = (state << 4) | ((state & 3) ^ cur)
        state |= cur << 2
    return state


def next_code(state, bits=26):
    code = 0
    for _ in range(bits):
        code = (code << 1) | (state & 1)
        state = ((state << 1) ^ (state >> 61)) & MASK
        state ^= MASK
        for j in range(0, 64, 4):
            cur = (state >> j) & 15
            changed = (cur >> 3) | ((cur >> 2) & 2) | ((cur << 3) & 8) | ((cur << 2) & 4)
            state ^= changed << j
    return state, code


def output_pair(seed):
    state, first = next_code(setup(seed))
    _, second = next_code(state)
    return (first << 26) | second


def recover_seed(first, second):
    observed = (first << 26) | second
    baseline = output_pair(0)
    effects = [output_pair(1 << bit) ^ baseline for bit in range(32)]
    rows = []
    for bit in range(52):
        mask = sum(((effect >> bit) & 1) << j for j, effect in enumerate(effects))
        rows.append([mask, ((observed ^ baseline) >> bit) & 1])

    pivots = {}
    for row in rows:
        while row[0]:
            bit = row[0].bit_length() - 1
            if bit not in pivots:
                pivots[bit] = row
                break
            row[0] ^= pivots[bit][0]
            row[1] ^= pivots[bit][1]
        else:
            if row[1]:
                raise ValueError("Codes do not match one generator state")

    if len(pivots) != 32:
        raise ValueError(f"Only {len(pivots)} of 32 seed bits are determined")
    seed = 0
    for bit in sorted(pivots):
        mask, value = pivots[bit]
        known = (mask & seed).bit_count() & 1
        seed |= (value ^ known) << bit
    if output_pair(seed) != observed:
        raise ValueError("Recovered seed did not reproduce the observations")
    return seed


def predict(first, second):
    seed = recover_seed(first, second)
    state = setup(seed)
    state, _ = next_code(state)
    state, _ = next_code(state)
    _, third = next_code(state)
    return third


if __name__ == "__main__":
    if len(sys.argv) == 1:
        sample = 0x12345678
        state = setup(sample)
        state, a = next_code(state)
        state, b = next_code(state)
        _, c = next_code(state)
        assert recover_seed(a, b) == sample
        assert predict(a, b) == c
        print("self-test passed")
    elif len(sys.argv) == 3:
        print(predict(int(sys.argv[1]), int(sys.argv[2])))
    else:
        raise SystemExit("usage: model-e1337-solver.py [first_code second_code]")

