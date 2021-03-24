#include <stdio.h>

void help() {
    printf("hello -print 'Hello World!'\nfibonacci <int> -Print fibonacci numbers up to <int>. Without args, will ask for the int.\nlist –list all the files in the current directory.\ncd <directory> –change the current directory to the <directory>. The default directory would be the directory where the shell program was invoked.\nhelp –display the internal commands and a short description on how to use them.\nquit –quit the shell program.\nhistory –display all the previous command entered into the shell program.\n");
}
