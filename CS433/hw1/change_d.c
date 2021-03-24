#include <stdio.h>
#include <unistd.h>

void cd(char* dir) {
    //http://man7.org/linux/man-pages/man2/chdir.2.html
    if (!chdir(dir)) {
        printf("You are now in the %s directory.\n", dir);
    }
    else {
        //https://linux.die.net/man/3/getcwd
        char* failure;
        printf("Directory change failed;\nyou are still in the %s directory.\n", getcwd(failure, 0));
    }
}
