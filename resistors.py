#!/usr/bin/env python

import argparse

E24 = [1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.7, 3.0, 3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.5, 8.2, 9.1]

def expand_series(series, minimum=0):
    expanded = []
    for f in [1, 10, 100, 1000, 10000, 100000, 1000000]:
        for v in series:
            val = v * f
            if val >= minimum:
                expanded.append(val)
    return expanded

# A = 1 + (R2/R1)

# A - 1 = R2 / R1

# R2 = (A - 1) * R1

def resistance_string(value):
    outval = value
    prefixes = [
            (1000000, 'M'),
            (1000, 'k'),
            (1, ''),
            ]
    fp = None
    for prefix in prefixes:
        fp = prefix
        if outval >= fp[0]:
            outval = outval / fp[0]
            break
    if outval < 10:
        outval = round(outval, 1)
    else:
        outval = round(outval)
    outstr = str(outval) + fp[1] + 'Ω'
    return outstr

def closest_matching(desired, series):
    #print(f'searching for closest value to {desired}')
    candidates = []
    for R in expand_series(series):
        diff = desired - R
        err = abs(diff / desired)
        #print(f'R={R} diff={diff} err={err}')
        candidates.append((R, err))

    candidates = sorted(candidates, key=lambda e: e[1])
    match = candidates[0][0]
    return match

def search(amplification, series, count, minimum):
    print(f'Searching for values for A = {amplification}')
    b = amplification - 1.0

    # R2 = b * R1

    # Try all values for R1

    candidates = []
    for r1 in expand_series(series, minimum):
        r2 = b * r1
        r2_matched = closest_matching(r2, series)
    
        err = (r2 - r2_matched) / r2

        candidates.append((r1, r2_matched, err))

    candidates = sorted(candidates, key=lambda c:abs(c[2]))
    for c in candidates[:count]:
    #for c in candidates:
        r1 = resistance_string(c[0])
        r2 = resistance_string(c[1])
        err = c[2]
        print(f'R1: {r1} -> R2: {r2} err: {err * 100:.2f}%')



if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Calculate resistor values for opamp amplifier circuit.')
    parser.add_argument('-a', '--amplification', type=float, required=True, help='Target amplification')
    parser.add_argument('-c', '--count', type=int, default=5, help='Number of results')
    parser.add_argument('-m', '--min', type=float, default=0, help='Minimum resistance value')
    args = parser.parse_args()

    search(args.amplification, E24, args.count, args.min)
