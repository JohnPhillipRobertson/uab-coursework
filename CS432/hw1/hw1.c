/******************************************************************************
*  Homework-1 - Sequential Program                                            *
*                                                                             *
*  To Compile: gcc -O hw1.c                                                   *
*  To run: ./a.out <size> <gens>                                                     *
*                                                                             *
*  Author: John Robertson                                                     *
*  Email: jprob@uab.edu                                                       *
*  Date: February 4, 2021                                                     *
******************************************************************************/
#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

double gettime(void) {
    struct timeval tval;
    gettimeofday(&tval, NULL);
    return((double)tval.tv_sec + (double)tval.tv_usec/1000000.0);
}

int **allocarray(int P, int Q) {
    int i;
    int *p, **a;

    p = (int *)malloc(P*Q*sizeof(int));
    a = (int **)malloc(P*sizeof(int*));

    if (p == NULL || a == NULL)
    printf("Error allocating memory\n");

    /* for row major storage */
    for (i = 0; i < P; i++) {
        a[i] = &p[i*Q];
    }
    return a;
}

int** initarray(int **a, int mrows, int ncols, int value) {
    int i,j;
    for (i=0; i<mrows; i++) {
        for (j=0; j<ncols; j++) {
            a[i][j] = (rand() % 2) * value;
        }
    }
    return a;
}

void printarray(int **a, int mrows, int ncols) {
    int i,j;
    for (i=0; i<mrows; i++) {
        for (j=0; j<ncols; j++) {
            printf("%d ", a[i][j]);
        }
        printf("\n");
    }
}

struct boards {
    int **now, **next;
};

int** transpose(int** a, int** b, int N, int PAD) {
    int i, j;
    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            int k = PAD/2;
            b[i + k][j + k] = a[i][j];
        }
    }
    return b;
}

int** game(struct boards* arg, int target_i, int target_j) {

    int** now_arr = arg->now;
    int** next_arr = arg->next;

    int total = 0;
    total += next_arr[target_i][target_j];
    total += next_arr[target_i+2][target_j+2];
    total += next_arr[target_i][target_j+1];
    total += next_arr[target_i+1][target_j];
    total += next_arr[target_i+2][target_j+1];
    total += next_arr[target_i+1][target_j+2];
    total += next_arr[target_i+2][target_j];
    total += next_arr[target_i][target_j+2];

    if (now_arr[target_i][target_j] == 1 && (total <= 1 || total >= 4)) {
        now_arr[target_i][target_j] = 0;
    }
    else if (total == 3) {
        now_arr[target_i][target_j] = 1;
    }

    return now_arr;
}


int main(int argc, char **argv) {
    int N, generations, i, j, k, PAD;
    int **a=NULL, **b=NULL;
    PAD = 2;

    if (argc != 3) {
        printf("Usage: %s <Board Size> <Generations>\n", argv[0]);
        exit(-1);
    }

    N = atoi(argv[1]);
    generations = atoi(argv[2]);

    /* Allocate memory for both matrices and temporary arrays */
    a = allocarray(N, N);
    b = allocarray(N + PAD, N + PAD);

    /* Initialize the matrices */
    /* All neighbors in the padding are zeroes, ghost cells */
    srand(123456);
    a = initarray(a, N, N, 1);
    b = initarray(b, N + PAD, N + PAD, 0);

    b = transpose(a, b, N, PAD);

    /* Perform game */

    //printf("Generation %d\n", 0);
    //printarray(a, N, N);
    //printf("\n");
    //printarray(b, N + PAD, N + PAD);
    //printf("\n");

    struct boards playing_field;
    playing_field.now = a;
    playing_field.next = b;

    double starttime = gettime();
    for (k = 0; k < generations; k++) {
        for (i = 0; i < N; i++) {
            for (j = 1; j < N; j++) {
                a = game(&playing_field, i, j);
            }
        }
        b = transpose(a, b, N, PAD);
        //printf("Generation %d\n", k + 1);
        //printarray(a, N, N);
        //printf("\n");
        //printarray(b, N + PAD, N + PAD);
        //printf("\n");
    }
    double endtime = gettime();
    printf("Time taken = %lf seconds\n", endtime-starttime);

    free(a);
    free(b);

    return 0;
}
