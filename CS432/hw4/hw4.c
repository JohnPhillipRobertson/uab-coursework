/******************************************************************************
*  Homework-4 - Message-Passing Program                                       *
*                                                                             *
*  To Compile: gcc -O hw4.c                                                   *
*  To run: ./a.out <size> <gens>                                              *
*                                                                             *
*  Author: John Robertson                                                     *
*  Email: jprob@uab.edu                                                       *
*  Date: April 6, 2021                                                        *
******************************************************************************/
#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <mpi.h>

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
    struct boards playing_field;
    PAD = 2;
    int ierr, num_procs, my_id, x_to_receive, y_to_receive;
    MPI_Status status;

    ierr = MPI_Init(&argc, &argv);
    ierr = MPI_Comm_rank(MPI_COMM_WORLD, &my_id);
    ierr = MPI_Comm_size(MPI_COMM_WORLD, &num_procs);

    if (my_id == 0) {
        if (argc != 3) {
            printf("Usage: %s <size> <max. iterations>\n", argv[0]);
            MPI_Abort(MPI_COMM_WORLD, EXIT_FAILURE);
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


        playing_field.now = a;
        playing_field.next = b;
        double starttime = gettime();

        for (k = 0; k < generations; k++) {

            int peer = (my_id == 0) ? 1 : 0;

            MPI_Sendrecv(&a, 1, MPI_INT, peer, 0, //what type should this be? MPI_INT intuitively isn't it; I'm sending an int**
                         &a, 1, MPI_INT, peer, 0,
                         MPI_COMM_WORLD, MPI_STATUS_IGNORE);

            for (i = 0; i < N; i++) {
                for (j = 1; j < N; j++) {
                    a = game(&playing_field, i, j);
                }
            }


            b = transpose(a, b, N, PAD);
            printf("Generation %d\n", k + 1);
            printarray(a, N, N);
            printf("\n");
            printarray(b, N + PAD, N + PAD);
            printf("\n");
        }
        double endtime = gettime();
        printf("Time taken = %lf seconds\n", endtime - starttime);

        free(a);
        free(b);
    }

    else {
        ierr = MPI_Recv( &x_to_receive, 1, MPI_INT, 0, 2001, MPI_COMM_WORLD, &status);
        ierr = MPI_Recv( &y_to_receive, 1, MPI_INT, 0, 2001, MPI_COMM_WORLD, &status);
        a = game(&playing_field, x_to_receive, y_to_receive);
        ierr = MPI_Send( &a, 1, MPI_LONG, 0, 2002, MPI_COMM_WORLD);
    }


    ierr = MPI_Finalize();
}
