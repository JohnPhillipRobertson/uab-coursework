.data
input_message:.string "Enter a numbers:\n"
input: .string "%i"
buffer: .space 10

.text
.global main

main:
	movq $input_message, %rdi
	movq $0, %rax #Making rax 0 otherwise Segmentation fault occurs.
	call printf #Printing input message
	
	movq $input, %rdi
	movq $buffer, %rsi #Buffer is used to store data that isn’t known yet.
	movq $0, %rax
	call scanf #Calling Scanf for user input.
	ret
	