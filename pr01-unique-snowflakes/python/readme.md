# Unique Snowflakes

> ref: This is [DMOJ problem cco07p2](<https://dmoj.ca/problem/cco07p2>).
>
> Canadian Computing Competition: 2007 Stage 2, Day 1, Problem 2

You may have heard that no two snowflakes are alike. Your task is to write a program to determine whether this is really true. Your program will read information about a collection of snowflakes, and search for a pair that may be identical.

Each snowflake has six arms. For each snowflake, your program will be provided with a measurement of the length of each of the six arms. Any pair of snowflakes which have the same lengths of corresponding arms should be flagged by your program as possibly identical.

>*Note*: The original CCO data were weak and have been augmented with some custom test cases.

## Input Specification

- The first line of input will contain a single integer $0 < n \le 100,000$  the number of snowflakes to follow.
- This will be followed by lines, each describing a snowflake. Each snowflake will be described by a line containing six integers (each integer $0 \le n < 10,000,000$), the lengths of the arms of the snowflake.
  - The lengths of the arms will be given in order around the snowflake (either clockwise or counterclockwise), but they may begin with any of the six arms. For example, the same snowflake could be described as `1 2 3 4 5 6` or `4 3 2 1 6 5`.

## Output Specification

- If all of the snowflakes are distinct, your program should print the message: `No two snowflakes are alike`.

- If there is a pair of possibly identical snowflakes, your program should print the message: `Twin snowflakes found`.

## Sample Input

```txt
2
1 2 3 4 5 6
4 3 2 1 6 5
```

## Output for Sample Input

```txt
Twin snowflakes found.
```

## Snowflake representation

The snowflake can be viewed as a polinomial where the arms are the coefficients
in ascending order of power:

$k_0 + k_1X + K_2X^2 + ... + K_5X^5$ for $X = 10,000,001$ and $0 \leq K_i < 10,000,001$

### Normalization

Since the snoflake `1 2 3 4 5 6` is the same as `4 5 6 1 2 3`, we can define
normalization as the process of rotating the snowflake until the value of the polynomial reaches its minimum.

### Twins

Two snowflakes are twins if their normalized value is the same.

## Strategy

In Python, with big-integer precision available, it is possible to generate
all values, sort the list, and check for duplicates.

You could also use a hashset and check if the calculated value (of the normalized
snowflake) is in the pool of viewed snowflakes and stop at the first twin.
