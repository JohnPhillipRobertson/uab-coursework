#Write an assembly language program to input side of a triangle and check whether triangle is valid or not. A triangle is valid if sum of its two sides is greater than the third side. Means if a, b, c are three sides of a triangle, then the triangle is valid if all three conditions are satisfied: a + b > c, a + c > b, b + c > a.
.data
input_message1: .string "Enter a number:\n"
input_message2: .string "Enter another number:\n"
input_message3: .string "Enter a final number:\n"
input: .string "%i"
output_message1: .string "The triangle is invalid.\n"
output_message2: .string "The triangle is valid.\n"
buffer1: .space 10
buffer2: .space 10
buffer3: .space 10

.text

.global main
main:
	movq $input_message1, %rdi
	movq $0, %rax
	call printf
	
	movq $input, %rdi
	movq $buffer1, %rsi # the user input gets stored in the buffer
	movq $0, %rax
	call scanf
	
	movq $input_message2, %rdi
	movq $0, %rax
	call printf
	
	movq $input, %rdi
	movq $buffer2, %rsi
	movq $0, %rax
	call scanf
	
	movq $input_message3, %rdi
	movq $0, %rax
	call printf
	
	movq $input, %rdi
	movq $buffer3, %rsi
	movq $0, %rax
	call scanf
	
	movq (buffer1), %rsi
	movq (buffer2), %rdi
	addq (buffer3), %rdi
	cmpq %rdi, %rsi
	jg .invalid
	
	movq (buffer2), %rsi
	movq (buffer3), %rdi
	addq (buffer1), %rdi
	cmpq %rdi, %rsi
	jg .invalid
	
	movq (buffer3), %rsi
	movq (buffer1), %rdi
	addq (buffer2), %rdi
	cmpq %rdi, %rsi
	jg .invalid
	jmp .valid
	
	.invalid:
		movq $output_message1, %rdi
		movq $0, %rax
		call printf
		jmp .end
	.valid:
		movq $output_message2, %rdi
		movq $0, %rax
		call printf
	.end:
	ret
