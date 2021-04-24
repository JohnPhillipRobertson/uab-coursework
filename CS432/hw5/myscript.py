#!/bin/bash
import subprocess
for k in range(5):
	for j in range(5, 21):
		acc = 0.0
		for i in range(3):
			acc += float(subprocess.check_output(
				f"mpiexec -np {2**k} ./a.out {2**j}",
				shell=True
			))
		acc /= 3
		print(f"Average time taken for {2**k} processes, {2**j} bytes: {acc}")
	print("")