.data
buffer1: .quad 4
buffer2: .quad 2

.text

.global main
main:
	#A*B + A/B
	movq $buffer1, %rsi
	movq $buffer2, %rbx
	imulq %rsi, %rbx #a * b
	
	movq $buffer1, %rax
	movq $buffer2, %rsi
	xorq %rdx, %rdx
	idiv %rsi #a / b
	
	addq %rbx, %rsi #add them
	
	movq %rsi, %rdi
	movq $0, %rax
	call printf
	#A+B - A-B
	movq $buffer1, %rsi
	movq $buffer2, %rbx
	addq %rsi, %rbx #a + b
	
	movq $buffer2, %rdi
	subq %rsi, %rdi #a - b
	
	subq %rbx, %rdi #subtract them
	
	movq $0, %rax
	call printf
	
	ret
