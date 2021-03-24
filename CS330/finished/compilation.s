# A lot of assembly comes down to understanding the code you write- it is unreasonable to write the code and test it repeatedly by running it. Instead, you must build an understanding of each instruction you use and understand what will go wrong under some circumstances and avoid such situations.
# However, some issues are much more easily fixed, as you are directly informed before a runnable program can be created. Attempting to compile will give you a list of errors and their corresponding line numbers.
# In this "program" (it won't work at the end, but it won't have any compilation errors, importantly), we will see both compilation errors and runtime errors. You may fix both, but you are only expected to fix the compilation errors.

.global main
.text

main:

int_arr: .int 92, 44, 11, 22
# this generates a warning. what does it do?
# is there a reason we wouldn't want this behavior?

movq %rax, %rcx


movzwq %ax, %rax


movl %ebx, %ecx


inc %rsp
# this is a valid instruction,
# but will almost certainly cause unexpected problems
# how can it be corrected?
dec %rsp


imul %rdx, %rax


imul %rbx
# this is actually a valid instruction
# but what will it do? Implicitly multiply by %rax


imul %rdx, %rbx
# same here- think about what registers will be multiplied, and where all the results will be stored

xorq %rdx, %rdx
idiv %rcx   
# this one has one more issue than just the compiler error
# spot and fix it too! Btw, remainder goes in %rdx


div %rbx
# this function works, but it is here because it is important to know:
# what is the difference between div and idiv? div is unsigned.


sub $8, %rcx
# this may not behave as intended, even though it compiles. why?


movq -4(%rax, %rbx, 8), %rcx
# there are two problems that will occur here. Identify and fix both.


syscall
int $0x80
# what is the difference between the above two instructions?
# which should you use in your programs? First is 64, 2nd 32 bit. Use former.

start_func:
    push %rax
    push %rbx
middle_func:
    # do whatever we want here
end_func:
    pop %rax
    pop %rbx
    ret
    # what will the unintended behavior be in this function, even though it will execute correctly? %rax and %rbx will swap.

new_func:
    push %rdx
    push %rcx
finally:
    pop %rcx
    pop %rdx
    #pop %rax
    ret
# this will not execute correctly. what will go wrong? Stack is empty. Seg fault's gonna happen.

call new_func
jmp new_func
# what is the difference between the two of these? Call means push pointer to stack. Calling pop one time too many leads to the stack pointer showing the call being removed before ret is called.
# what will go wrong if we jump to a function? Infinite loop could happen.
