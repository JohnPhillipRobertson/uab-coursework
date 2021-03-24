# global data  #
#Dr. Unan said I could use this
    .data
format: .asciz "%d\n"
.text
	.global main
main:
	nop
printit:
	pushq %rbx
	leaq format(%rip), %rdi
	movl $1, %esi	#Writing to ESI zero extends to RSI.
	xorl %eax, %eax	#Zeroing EAX is efficient way to clear AL.
	call printf
	popq %rbx
	ret
