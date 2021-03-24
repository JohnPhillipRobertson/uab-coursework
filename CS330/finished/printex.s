.text
	
	.global _start


_start:
	
	movq $4, %rax  #move the int 4 into the rax register (the "a" register, but all 64 bits of it!)
	
	movq $1, %rbx  # move 1 into the rbx register
	
	movq $msg, %rcx  # move our message into rcx
	
	movq $len, %rdx  # move the length of the message into rdx


# All these things are necessary to print out data! The first two are especially important.


# We moved 1 into %rbx because it is the "stdout" file descriptor,

# meaning it tells the system we are trying to output something.


# We moved 4 into %rax because it is the system call corresponding to printing information.

# To be exact, it is "sys_write", and it is necessary to tell the operating system we 

# are writing to a file descriptor, which was defined above:
stdout.


	
	int $0x80  #syscall
	
	# You won't need to do this all the time, but here we are performing a system interrupt.
	
	# What this does is tell the OS that we want our program's instructions to be looked at and executed.
	
	# Our program, and all others, rely upon the OS to do a lot of work.
	
	# When we call on it, it will check the 'a' register for any system calls (like the 4 in rax above)
	
	# and execute them.


	
	movq $1, %rax
	
	movq $0, %rbx

	
	# Lastly, we put 1 in rax, which is sys_exit. It is the sys_exit call, which will end the program.
	
	# But we also need to make sure that the 'b' register is zero; rbx would hold an error code of some sort
	
	# if something went wrong.

	
	int $0x80
	
	# Call the kernel, tell it to perform the above work
!

msg:
	
	.ascii "Hello World\n"
	
	len = . - msg
