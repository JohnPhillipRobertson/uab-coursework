# 

This program lists subdirectories of the inputted directory according to rules set forth by the command line arguments

## Compilation

```bash
gcc p2.c
```

## Usage


```bash
$ ./a.out
```

Will list all of the directories in the current directory.

This is the only way to run it without using a filename argument; if you want to use the current directory and the available flags, you must write "." as the directory argument.

```bash
$ ./a.out . -S
```

Will also list the regular files and symbolic links in the current directory. Note that it will only do that, and not descend further into the directory hierarchy.

```bash
$ ./a.out . -f main
```

Will only list files that contain the substring "main."

```bash
$ ./a.out . -s 1024
```

Will only list files that are larger than 1024 bytes.

Note that you can combine arguments in any order, like so:

```bash
$ ./a.out . -s 1024 -S -f main
```

## Sources
For how to find the referents of symbolic links: https://wiki.sei.cmu.edu/confluence/display/c/POS30-C.+Use+the+readlink%28%29+function+properly
For how to get the size of a file for the sake of comparison: https://stackoverflow.com/questions/238603/how-can-i-get-a-files-size-in-c
For how to use getopt: https://www.gnu.org/software/libc/manual/html_node/Example-of-Getopt.html
