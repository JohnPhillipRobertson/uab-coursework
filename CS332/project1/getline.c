/* Sample program to illustrate C standard library usage */
/* This program uses the getline function to read a line at a time from the 
 * standard input. Look at the man page for getline (man 3 getline) for 
 * more details.
 */
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv) {
	char *line=NULL;
	size_t maxlen=0;
	ssize_t n;

	/* read till end of file (type Control-D to stop) */
	while ( (n = getline(&line, &maxlen, stdin)) > 0) {
		printf("No. of characters read = %ld\n", n);
		printf("Size of buffer allocated = %ld\n", maxlen);
		printf("Line read:\n[%s]", line);
	}

	free(line);
	return 0;
}

