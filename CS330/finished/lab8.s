.include "functions.s"
.text
.data
	movq $.example, %rdx
	movq $7, %rsi #length of array in rsi
	.example:
		.string "example"
.global main
main:
	movq $.example, %rdi #array in rdi
	subq %rdi, %rdx
	cmpq $7, %rdi
	jg .end
	call inc_and_print
	inc %rdi
	jmp main:
inc_and_print:
	push %rsi
	push %rdi
	movq $c, %rsi
	call printr
.end:
	ret
