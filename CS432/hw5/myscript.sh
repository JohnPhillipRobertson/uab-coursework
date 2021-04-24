for k in {0..4}
do
	for j in {5..20}
	do
		ACC=0.0
		for i in {0..2}
		do
			((ACC=$ACC+$(mpiexec -np $((2**$k)) ./hw5 $((2**$j)))))
		done
		((ACC=$ACC/3))
		echo "Average time taken for 2^$k processes, 2^$j bytes: $ACC\n"
	done
	echo "\n"
done