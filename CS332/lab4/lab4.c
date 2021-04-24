#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#define     BUFFSIZE 4096
int main(int argc, char *argv[]) {
    int  file_one, file_two;
    long int n;
    char buf[BUFFSIZE];
    if (argc != 3){
        printf("Usage: %s <source_filename> <destination_filename>\n", argv[0]);
        exit (-1);
    }
    //http://man7.org/linux/man-pages/man2/open.2.html
    //How to use O_APPEND
    file_one = open(argv[1], O_WRONLY|O_APPEND);
    file_two = open(argv[2], O_RDONLY);
    if (file_one == -1 || file_two == -1){
        printf("Error with file open\n");
        exit (-1);
    }
    while ((n = read(file_two, buf, BUFFSIZE)) > 0){
        if (write(file_one, buf, n) != n){
            printf("Error writing to output file\n");
            exit (-1);
        }
    }
    if (n < 0){
        printf("Error reading input file\n");
        exit (-1);
    }
    close(file_one);
    close(file_two);
    return 0;
}
