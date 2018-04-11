# Proof of Work

**Author:** Matthew Hartshorn

This project illustrates the basic principles of [Proof-of-Work](https://en.wikipedia.org/wiki/Proof-of-work_system) (POW) used in cryptocurrency and blockchain technologies. Utilizing SHA256 hashing agorithim this project is capable of determining a usuable solution to solve POW requirements. The script works using single thread iteration to find and verify a viable solution for the given POW target value.  


# Environment

The following information denotes the environment setup in which the code was written and tested.

**Language:** Python 3.5+

**Operating System:** Windows 10


# Prerequisites

The Python 3.5+ command line interface must be installed on the device. The download for Python can be found [here](https://www.python.org/downloads/).

**Cryptography** - Python encryption library
```bash
> pip install cryptography
```


# Usage

Run Python followed by the script `pow.py` then specify which command you want to run and any required arguments.

```
> python pow.py

usage: pow.py [-h [CMD]] {target,solve,verify} ...

positional arguments:
  {target,solve,verify}
                        Commands
    target              Generates the POW target value
    solve               Attempts to solve the POW problem given input data and
                        a target difficulty
    verify              Checks if the provided solution is satisfies the
                        difficulty requirements from the given target

optional arguments:
  -h [CMD], --help [CMD]
                        Shows this help message or command help and exit
```


# Commands

## Target

**Command:** `target`

**Description:**  
Generates a POW target value based on the provided difficulty value. The difficulty is the number of leading bits set to 0, in the resulting SHA256 hash value. All subsiquent bits of the target are set to 1. The output is the hexadecimal representation of the binary sequence.

**Options:**

| Char | Verbose     | Arg       | Description
| ---- | ----------- | --------- | -------------------------------------------- |
| `-o` | `--output`  | `FILE`    | The file in which the output will be written

**Arguments:**

| Argument | Required | Description
| -------- | -------- | ---------------------------------------- |
| `target` | Yes      | The number of bits to be set to zero for the target difficulty, 0 - 256

**Usage:**  
```
target [-o FILE] <target>
```

**Examples:**  
```
> python pow.py target 20
00000fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff

> python pow.py target 20 -o ./data/target.txt
```


## Solve

**Command:** `solve`

**Description:**  
Attempts to find a solution to the POW based on the provided data that needs to be hashed and desired target value.

**Options:**

| Char | Verbose     | Arg       | Description
| ---- | ----------- | --------- | -------------------------------------------- |
| `-o` | `--output`  | `FILE`    | The file in which the output will be written
| `-i` | `--input`   | `FILE`    | The input file that will be hashed
| `-m` | `--message` | `MSG`     | The input message that will be hashed

> **Note:** Either -i or -m are require, but both cannot be provided

**Arguments:**

| Argument | Required | Description
| -------- | -------- | ---------------------------------------- |
| `target` | Yes      | The file that contains the difficulty target

**Usage:**  
```
solve [-o FILE] [-m MSG|-i FILE] <target>
```

**Examples:**  
```
> python pow.py solve -m test ./data/target.txt
Data: test
================================================================================
Hash: 00000bfd28e2197b2d3aaf9e924ec57d12549d78e509a07bbda322a00a60b079
Solution: 2125381

> python pow.py solve -i ./data/input.txt ./data/target.txt
Data: test
================================================================================
Hash: 00000bfd28e2197b2d3aaf9e924ec57d12549d78e509a07bbda322a00a60b079
Solution: 2125381

> python pow.py solve -i ./data/input.txt -o ./data/solution.txt ./data/target.txt
```



## Verify

**Command:** `verify`

**Description:**  
Verifies that the provided solution is a valid POW for the given data and difficulty target.

**Options:**

| Char | Verbose     | Arg       | Description
| ---- | ----------- | --------- | -------------------------------------------- |
| `-i` | `--input`   | `FILE`    | The input file that will be hashed
| `-m` | `--message` | `MSG`     | The input message that will be hashed

> **Note:** Either -i or -m are require, but both cannot be provided

**Arguments:**

| Argument   | Required | Description
| ---------- | -------- | ---------------------------------------- |
| `solution` | Yes      | The file that contains the POW solution value
| `target`   | Yes      | The file that contains the difficulty target

**Usage:**  
```
verify [-m MSG|-i FILE] <solution> <target>
```

**Examples:**  
```
> python pow.py verify -m test ./data/solution.txt ./data/target.txt
1 (valid)

> python pow.py verify -i ./data/input.txt ./data/solution.txt ./data/target.txt
1 (valid)

> python pow.py verify -m "different data" ./data/solution.txt ./data/target.txt
0 (invalid)
```