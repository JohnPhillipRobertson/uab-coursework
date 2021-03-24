printr:
		push %rax
		push %rdi
        xor %rax, %rax
		call printf@PLT
		pop %rdi
		pop %rax
		ret	

# expects array pointer in %rdx
# expects array length in %rbx, in ITEMS, not bytes
# expects 32 bit values
# you may change this, but UPLOAD YOUR FUNCTIONS.S if you do
# format string in %rdi, which must be "%d"
printArr:
        push %rsi  # protect rsi, used for print
        push %rcx  # protect rcx, used for index
        push %rax  # protect rax, 0 for print
        xor %rax, %rax  # zero rax
        xor %rcx, %rcx  # zero rcx, init index

printLoop:
        push %rdi  # printf destroys the registers passed to it
        push %rdx  # including rdx
        push %rcx  # and rcx
        mov (%rdx, %rcx, 4), %rsi  # get first item of array, put in rsi
        call printf@PLT  # print; we assume correct string in rdi
        pop %rcx
        pop %rdx
        pop %rdi
        inc %rcx  # increase index
        cmpq %rbx, %rcx  # make sure we're not outside index
        jl printLoop  # if inside, print another elem

printFinished:
        pop %rax
        pop %rcx
        pop %rsi
        ret
