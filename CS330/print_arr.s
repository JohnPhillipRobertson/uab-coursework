.include "functions.s"
fmtint:
    .string "%d\n"
    .text    
    .global main

arr: .long 14, 22, 19, 17, 35, 6

main:
    movq $fmtint, %rdi  # format string
    movq $arr, %rdx  # pointer to array
    movq $6, %rbx  # len of string
    call printArr  # all the registers above are NECESSARY!

