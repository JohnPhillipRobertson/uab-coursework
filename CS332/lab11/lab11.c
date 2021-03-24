#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//
//https://stackoverflow.com/questions/9834067/difference-between-char-and-const-char
void shell(const char* input) {
    FILE *fp1;
    FILE *standard_out;
    char line[BUFSIZ];

    if ((fp1 = popen(input, "r")) == NULL) {
        perror("popen");
        exit(EXIT_FAILURE);
    }

    standard_out = fdopen(1, "w");

    while (fgets(line, BUFSIZ, fp1) != NULL) {
        if (fputs(line, standard_out) == EOF) {
            printf("Error writing to pipe\n");
            exit(EXIT_FAILURE);
        }
    }


    if (pclose(fp1) == -1) {
        perror("pclose");
        exit(EXIT_FAILURE);
    }


}

int main(int argc, char **argv) {
    /*
    CS 433's hw2 too similar,
    so I did not use it as a base,
    but I needed a reminder for how I handled user input
    in a loop in hw1, which doesn't even use processes.
    https://gitlab.cis.uab.edu/jprob/CS433-Homework-1
    */
    int running = 1;
    while(running) {
        char* line = NULL;
    	size_t maxlen = 0;
        printf("Enter command: ");
        getline(&line, &maxlen, stdin);
        if (strncmp("quit", line, 4) == 0) {
            printf("Exiting program...bye!\n");
            running = 0;
        }
        else {
            shell(line);
        }
    }

    return 0;
}

//Questions for Trupesh:
//Can I use my 433 shell as a base?
//How do you chain arbitrary pipes and redirections?
//maybe
//that's what popen and pclose are for; look at those examples.
