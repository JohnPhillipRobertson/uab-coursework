#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
#include <unistd.h>

#include "functions.h"

int main(int argc, char** argv) {
    int running = 1;
    while (running) {

        printf("uab_sh > ");
        char* line = NULL;
    	size_t maxlen = 0;
    	getline(&line, &maxlen, stdin);

        /*reading*/
        if (line[0] == '\n') {
            ;
        }
        else if (!strncmp("hello", line, 5)) {
            hello();
        }
        //https://stackoverflow.com/a/7021750/9295513
        else if (!strncmp("fibonacci", line, 9) && isspace(line[9]) && isdigit(line[10])) {
            char* input = strtok(line, " ");
            input = strtok(NULL, "");
            int in = (int) strtol(input, (char**)NULL, 10);
            fibwrapper(in);
        }
        else if (!strncmp("fibonacci", line, 9)) {
            free(line);
	    char* line = NULL;
	    printf("How many elements do you want to display?");
	    getline(&line, &maxlen, stdin);
            int in = (int) strtol(line, (char**)NULL, 10);
            fibwrapper(in);
        }
        else if (!strncmp("list", line, 4)) {
            list();
        }
        else if (!strncmp("cd", line, 2)) {
            char* input = strtok(line, " ");
            input = strtok(NULL, "\n");
            cd(input);
        }
        else if (!strncmp("help", line, 4)) {
            help();
        }
        else if (!strncmp("history", line, 7)) {
            history();
        }
        else if (!strncmp("quit", line, 4)) {
            running = 0;
        }
        else {
            printf("Invalid command. Try 'help' for help.\n");
        }
        /*end reading*/
        free(line);
    }
    return 0;
}
