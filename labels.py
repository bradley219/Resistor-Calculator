#!/usr/bin/env python3

# Test implementation of library functions

from resistors import resistance_string
from resistor_colors import resistor_color_bands
import sys

values = [10, 12, 15, 18, 20, 22, 24, 27, 30, 33, 36, 39, 43, 47, 51, 56, 62, 68, 75, 82, 91]
m_values = [1, 1.2, 1.5, 1.8, 2, 2.2, 4.7]
real_values = []

print("value,bands")

#real_values.append(0)

for value in values:
    v = value / 10
    real_values.append(v)
for value in values:
    v = value
    real_values.append(v)
for value in values:
    v = value * 10
    real_values.append(v)
for value in values:
    v = value * 100
    real_values.append(v)
for value in values:
    v = value * 1000
    real_values.append(v)
for value in values:
    v = value * 10000
    real_values.append(v)
for value in m_values:
    v = value * 1000000 
    real_values.append(v)

for v in real_values:
    rv = resistance_string(v, label='')
    bands = resistor_color_bands(v, num_bands=5, tolerance=1)
    bands = [b.name for b in bands]
    bands_str = ', '.join(bands)
    print(f"{rv},\"{bands_str}\"")


sys.exit(0)


for value in values:
    v = value / 10
    print(f"{v:.1f}")

for value in values:
    v = value
    print(f"{v:.0f}")

for value in values:
    v = value * 10
    print(f"{v:.0f}")

for value in values:
    v = value / 10
    print(f"{v:.1f}K")

for value in values:
    v = value
    print(f"{v:.0f}K")

for value in values:
    v = value * 10
    print(f"{v:.0f}K")

for value in [1, 1.2, 1.5, 1.8, 2, 2.2, 4.7]:
    v = value
    print(f"{v:.1f}M")
