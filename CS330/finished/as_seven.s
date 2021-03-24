#for I = 1 to A.length– 1
#	min = i
#	for J = I+1 to A.length
#		if A[J] < A[min]
#			min=j
#	if i!=min
#		swap A[min] and A[i]
.include "functions.s"
.text
	myarr: .quad 19, 10, 8, 17, 9
	sortedarr: .quad 0, 0, 0, 0, 0
.global	main
main:
	movq $myarr, %rdi
	movq $sortedarr, %rax
	movq $0, %rsi #i = 0
	mainLoop:
		inc %rsi
		movq (%rdi,%rsi,8), %rdx #min = i
		movq %rsi, %rcx #j = i
		innerLoop:
			inc %rcx
			cmovl (%rdi,%rcx,8), %rdx
			movq %rdx, (%rax, %rcx, 8) #put the sorted value into the array meant for sorting
			movq (%rdi,%rcx,8), %rsp
			pushq %rsi
			movq (%rax, %rcx, 8), %rsi
			cmpq %rsp, %rsi
			jne .swap #if i != min
			.swap:
				pushq (%rax, %rcx, 8)
				movq (%rdi, %rcx, 8), %rsp
				movq %rsp, (%rax, %rcx, 8)
				popq (%rdi, %rcx, 8)
			popq %rsi
			cmpq $5, %rcx #length of array
			jg innerLoop
		cmpq $4, %rsi #length of array - 1
		jg mainLoop
	movq %rax, %rdi
	call printArr
	ret
