.include "functions.s"
.data
	.global main
    c: .quad 7
	fmtstringOneContent: .string "no\0"
	fmtstringTwoContent: .string "yes\0"
main:
	movq $c, %rdi
is_prime: #uses rsi, rdi, rax, rdx, rcx
	movq $1, %rsi #initialize the "i" of the for loop
	movq %rdi, %rax
	loopThree:
		inc %rsi
		movq %rsi, %rcx
		xorq %rdx, %rdx #this is to be done before every division
		idiv %rcx #do a division here in order to take advantage of the remainder side effect
		cmpq $0, %rdx #remainder goes to rdx, so use it like a %
		jz noCondition #if input % i != 0 GOTO noCondition
		cmpq %rdi, %rsi
		jg yesCondition
		jmp loopThree
		noCondition:
			movq $fmtstringOneContent, %rsi
			call printr
			jmp endTwo
		yesCondition:
			movq $fmtstringTwoContent, %rsi
			call printr
		endTwo:
		ret
