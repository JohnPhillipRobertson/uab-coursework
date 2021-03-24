.text
	.global main
	a: .quad 2
	b: .quad 3
main:
	movq $a, %rdi
	movq $b, %rsi
loop:
	movq %rdi, %rax
	addq %rsi, %rax
	cmpq $15, %rax
	jg .end
	inc %rdi
	inc %rsi
	jmp loop
.end:
	ret
