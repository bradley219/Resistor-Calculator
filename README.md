# Resistor Values Calculator

General purpose tool for calculating potential resistor values to use in an opamp amplifier circuit.

## Usage

```
$ ./resistors.py -h

usage: resistors.py [-h] -a AMPLIFICATION [-c COUNT] [-m MIN]

Calculate resistor values for opamp amplifier circuit.

optional arguments:
  -h, --help            show this help message and exit
  -a AMPLIFICATION, --amplification AMPLIFICATION
                        Target amplification
  -c COUNT, --count COUNT
                        Number of results
  -m MIN, --min MIN     Minimum resistance value

```

## Example Output

```
$ ./resistors.py -a 10 -m 10000
Searching for values for A = 10.0
R1: 20kΩ -> R2: 180kΩ err: 0.00%
R1: 30kΩ -> R2: 270kΩ err: 0.00%
R1: 200kΩ -> R2: 1.8MΩ err: 0.00%
R1: 300kΩ -> R2: 2.7MΩ err: 0.00%
R1: 91kΩ -> R2: 820kΩ err: -0.12%
```
