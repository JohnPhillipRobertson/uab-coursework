printr:
		push %rax
		xor %rax, %rax
		call printf@PLT
		pop %rax
		ret	
