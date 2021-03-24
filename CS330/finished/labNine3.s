.data
input_message1: .string "Enter a number:\n"
input_message2: .string "Enter another number:\n"
input: .string "%i"
output_message: .string "The sum is %i\n"
buffer1: .space 10
buffer2: .space 10

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
	
	movq $output_message, %rdi
	movq (buffer1), %rsi
	movq (buffer2), %rbx
	addq %rbx, %rsi
	movq $0, %rax
	call printf
	ret
