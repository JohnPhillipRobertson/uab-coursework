.include "functions.s"  # YOU MUST HAVE THIS

.fmtint:
		.string "%d" # does NOT need \0

.fmtstr:
		.string "%s"

.bad:
		.ascii "example\0"
		
		.global main

main:
		# Step 1: Move a pointer to a string, or an integer into %rsi
		# Step 2: Move a format string, same as for the printf function, into %rdi
				# This can be ANY format string, but for simplicity, 
				# use %d for ints and %s for strings
		# Step 3: call printr	

		movq $17, %rsi		# first argument: the thing to be printed. 
						    # strings need a \0, or Null Terminator
		movq $.fmtint, %rdi # second argument: the format string
						    # these need to be strings, but do NOT need a null terminator
		call printr
