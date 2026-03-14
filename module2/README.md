# Module 2 — Control Flow & Conditionals

## Author
Wisdom Isaac Oku

## GitHub Username
educeptis-coder

## Description
This module covers control flow in Python — specifically how to make decisions in code using conditional statements. Each exercise builds on the ability to evaluate conditions and direct the program to execute different blocks of code based on those conditions.

## What I Learned

### 1. The `random` Module
- How to import and use Python's built-in `random` module
- Using `random.randint(a, b)` to generate a random integer between two values (inclusive)
- Using `random.seed()` to make random results reproducible for testing

### 2. Conditional Statements (`if / elif / else`)
- How to use `if` to check a condition
- How to use `elif` (else if) to check additional conditions when the first is false
- How to use `else` as a fallback when no conditions are met
- Covering all possible cases: positive, zero, and negative numbers

### 3. Clean Code Practices
- Writing logic directly in a file without wrapping it in functions
- Matching exact output formats required by test files
- Understanding how `exec()` and `open()` are used in test files to run and evaluate code

## How to Run

```bash
python3 1-main.py
```

## Expected Output
```
0 is zero
```
> Note: Output varies depending on the random seed. The logic handles all three cases: positive, zero, and negative.

## Files
| File | Description |
|------|-------------|
| `1-positive_or_negative.py` | Main exercise — generates a random number and prints whether it is positive, zero, or negative |
| `1-main.py` | Test file — sets a random seed and runs the exercise file |
| `README.md` | This file — describes the module and what was learned |
