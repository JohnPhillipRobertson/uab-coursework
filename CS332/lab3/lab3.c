#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void strsort(char** str, int len);

void strsort(char** str, int len) {
    int currLoc, i;
    char* temp;
    for (i = 0; i < len; i++) {
        currLoc = i;
        /*http://www.cplusplus.com/reference/cstring/strcmp/*/
        //Showed me how to use strcmp, specifically by its output
        while (currLoc > 0 && strcmp(str[currLoc - 1], str[currLoc]) > 0) {
            temp = str[currLoc];
            str[currLoc] = str[currLoc - 1];
            str[currLoc - 1] = temp;
            currLoc--;
        }
    }
}

int main() {

    int N, M, i;

    printf("Enter how many strings: ");
    scanf("%d", &N);
    printf("Okay. Taking in %d strings.\n", N);
    char** arr = (char**) malloc(N+1 * sizeof(char*));

    for (i = 0; i < N; i++) {
        printf("Enter length of the string: ");
        scanf("%d", &M);
        char *str = (char*) malloc(M+1 * sizeof(char));
        printf("Please enter your string: ");
        scanf("%s", str);
        arr[i] = str;
    }

    strsort(arr, N);

    printf("String array is sorted.\n");
    for (i = 0; i < N; i++) {
        printf("%s\n", arr[i]);
    }

    return 0;
}