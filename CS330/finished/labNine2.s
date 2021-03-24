.data
input_message: .string "Enter a number:\n"
input: .string "%i"
output_message: .string "The number is %i"
buffer: .space 10

.text

.global main
main:
	movq $input_message, %rdi
	movq $0, %rax
	call printf
	
	movq $input, %rdi
	movq $buffer, %rsi
	movq $0, %rax
	call scanf
	
	movq $output_message, %rdi
	movq (buffer), %rsi # dereferencing; move value in buffer into rsi
	movq $0, %rax
	call printf
	ret
