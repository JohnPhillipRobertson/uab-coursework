# 

This program takes in a file listing households and sorts either on price or host names.

## Compilation

```bash
gcc write_list.c
```

## Usage

```bash
./a.out
Do you want to sort on
1: price
or
2: host name?
1 # Will create a new file called listings_sorted.csv with the listings sorted on price.
```

## Sources
For how to pass structs into functions: https://stackoverflow.com/a/5865594/9295513
For how to use fopen: http://www.cplusplus.com/reference/cstdio/fopen/
