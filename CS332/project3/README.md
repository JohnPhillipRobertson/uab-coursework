#

This program lists subdirectories of the inputted directory according to rules set forth by the command line arguments, *including an argument that runs commands on the files*.

## Compilation

```bash
gcc p3.c
```

## Usage


```bash
$ ./a.out
```

Will list all of the files in the current directory.

```bash
$ ./a.out -S
```

Ditto the above, but with their sizes in bytes included.

```bash
$ ./a.out -f <bar>
```

Will only list files that contain the substring "bar."

```bash
$ ./a.out -s <int>
```

Will only list files that are larger than the given number of bytes.

```bash
$ ./a.out -s <int>
```

Note that you can combine arguments in any order, so long as -e is last, like so:

```bash
$ ./a.out -s 1024 -S -f main -e ls
```

## Sources

https://stackoverflow.com/a/298518/9295513