#Write a program in assembly language to find the Greatest Common Divisor of two numbers. You may use any version of the greatest common divisor algorithm, including choosing between linear and recursive versions of the algorithm. So long as the final result is correct, this is acceptable.
#while b != 0:
#        a, b = b, a%b
#    return a
.include "functions.s"
.text
.data
	.format:
		.string "%d\n"
.global main
main:
	movq $44, %rsi
	movq $99, %rdi
	.whileLoop:
		movq %rsi, %rax
		pushq %rdi
		xorq %rdx, %rdx
		idivq %rdi
		movq %rdx, %rdi
		popq %rsi
		cmpq $0, %rdi
		jnz .whileLoop
	movq $.format, %rdi
	call printr #expected output 11
	movq %rsi, %rax
	ret
