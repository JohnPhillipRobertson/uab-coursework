#Write an assembly language program to find whether an input number is even or odd.
.data
input_message: .string "Enter a number:\n"
input: .string "%i"
output_message1: .string "The number is odd.\n"
output_message2: .string "The number is even.\n"
buffer: .space 10

.text

.global main
main:
	movq $input_message, %rdi
	movq $0, %rax
	call printf
	
	movq $input, %rdi
	movq $buffer, %rsi
	movq $0, %rax
	call scanf
	movq (buffer), %rsi
	
	xorq %rdx, %rdx
	movq %rsi, %rax
	movq $2, %rsi
	idiv %rsi
	cmpq $1, %rdx
	je .odd
	.even:
		movq $output_message2, %rdi
		movq $0, %rax
		call printf
		jmp .end
	.odd:
		movq $output_message1, %rdi
		movq $0, %rax
		call printf
	.end:
		movq %rsi, %rax
		ret
