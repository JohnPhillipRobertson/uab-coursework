## CS 332 Lab 12

This program schedules jobs for as many processors as has your system, as well as letting you see which ones are currently running or not.

## Author
John Robertson

## Getting started

To compile:
```bash
make
```
or
```bash
gcc -o p4 p4.c queue.c
```

To run:
```
./p4 <int between 1 and nproc inclusive>
```

## Usage

The command
```bash
./p4 <int> space
```
will start the scheduler with a fixed amount of processes. If you do not know how many processors you have, use `nproc`.

Within the launched shell, you may use two commands, `showjobs` and `submit <string>`, as well as `quit` to quit. `showjobs` should show the current jobs running. `submit` will take your job to run. **NOTE**: You *must* include a trailing space ' ' after submitting a job, or it will not work properly.

**NOTE**: This program doesn't work.

## Sources

Dr. Bangalore's queue structure.

https://stackoverflow.com/a/19724773/9295513

https://linuxprograms.wordpress.com/2008/01/23/piping-in-threads/

## Contact Information

jprob@uab.edu
