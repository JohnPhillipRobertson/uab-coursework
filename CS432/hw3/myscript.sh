#!/bin/bash
echo -n "hw1"
./hw1 1000 1000
./hw1 5000 1000
./hw1 5000 5000
./hw1 10000 1000
./hw1 10000 10000
echo -n "hw3 2 threads"
module load intel
./hw3 1000 1000 2
./hw3 5000 1000 2
./hw3 5000 5000 2
./hw3 10000 1000 2
./hw3 10000 10000 2
echo -n "hw3 20 threads"
./hw3 1000 1000 20
./hw3 5000 1000 20
./hw3 5000 5000 20
./hw3 10000 1000 20
./hw3 10000 10000 20
echo -n "hw3 200 threads"
./hw3 1000 1000 200
./hw3 5000 1000 200
./hw3 5000 5000 200
./hw3 10000 1000 200
./hw3 10000 10000 200