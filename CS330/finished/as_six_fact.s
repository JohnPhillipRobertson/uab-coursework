.include "functions.s"
.output:
	.string "%i \n"
.global main
main:
	movq $4, %rdi
factorial: #uses rdi, rsi, rax
	movq %rdi, %rax
	movq %rdi, %rsi
	dec %rsi
	loopOne:
		imulq %rsi, %rax
		dec %rsi #for rsi to decrease every time it passes
		jz loopOne #rsi will never become zero and zero out rax
		movq %rax, %rsi
		movq .output, %rdi
		movq $0, %rax
		call printr
		movq %rsi, %rax
		ret
