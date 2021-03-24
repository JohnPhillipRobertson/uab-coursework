.include "functions.s"
.data
	.global main
    b: .quad 9
main:
	movq $b, %rdi
fibonacci: #uses rdi, rsi, rdx, rcx
	movq $0, %rsi
	movq $1, %rdx #this and the line above are the i1 and i2 of the sequence
	movq $0, %rcx #this is the "i" of the loop
	loopTwo:
		inc %rcx
		pushq %rdx #temporary
		addq %rsi, %rdx # i2 = i2 + i1
		popq %rsi #i1 = i2
		cmpq %rdi, %rcx
		jg loopTwo
		movq %rsi, %rax #I think that this is the element of the sequence I want to return
		call printr
		ret
