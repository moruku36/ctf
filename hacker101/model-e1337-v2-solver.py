"""Recover the Model E1337 v2 state from one disclosed 64-bit code.

The server's setup() and next() are affine maps over GF(2).  One 64-bit
output determines the effective 32-bit seed.  A second output can validate
the prediction before submitting the third code.

Usage: python model-e1337-v2-solver.py FIRST_CODE [SECOND_CODE]
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


def next_code(state):
    code = 0
    for _ in range(64):
        code = (code << 1) | (state & 1)
        for _ in range(3):
            state = ((state << 1) ^ (state >> 61)) & MASK
            state ^= MASK
            for j in range(0, 64, 4):
                cur = (state >> j) & 15
                changed = (cur >> 3) | ((cur >> 2) & 2) | ((cur << 3) & 8) | ((cur << 2) & 4)
                state ^= changed << j
    return state, code


def first_output(seed):
    return next_code(setup(seed))[1]


def recover_seed(observed):
    baseline = first_output(0)
    effects = [first_output(1 << bit) ^ baseline for bit in range(32)]
    rows = []
    for bit in range(64):
        mask = sum(((effect >> bit) & 1) << j for j, effect in enumerate(effects))
        rows.append([mask, ((observed ^ baseline) >> bit) & 1])

    pivots = {}
    for mask, value in rows:
        while mask:
            bit = mask.bit_length() - 1
            if bit not in pivots:
                pivots[bit] = (mask, value)
                break
            mask ^= pivots[bit][0]
            value ^= pivots[bit][1]
        else:
            if value:
                raise ValueError("Observed code does not match this generator")

    if len(pivots) != 32:
        raise ValueError(f"Only {len(pivots)} of 32 seed bits are determined")
    seed = 0
    for bit in sorted(pivots):
        mask, value = pivots[bit]
        seed |= (value ^ ((mask & seed).bit_count() & 1)) << bit
    if first_output(seed) != observed:
        raise ValueError("Recovered seed failed validation")
    return seed


def predict(first, count):
    state = setup(recover_seed(first))
    codes = []
    for _ in range(count):
        state, code = next_code(state)
        codes.append(code)
    return codes


if __name__ == "__main__":
    if len(sys.argv) not in (2, 3):
        raise SystemExit("usage: model-e1337-v2-solver.py FIRST_CODE [SECOND_CODE]")
    first = int(sys.argv[1])
    codes = predict(first, 3)
    if len(sys.argv) == 3 and codes[1] != int(sys.argv[2]):
        raise SystemExit("second code does not match: stream changed or first leak was not code 1")
    print(f"next code: {codes[2]:020d}")

