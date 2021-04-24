/******************************************************************************
*  Homework-5 - Implement Collective Communication Operation                  *
*                                                                             *
*  To Compile: mpicc hw5.c                                                    *
*  To run: Use the attached Python script                                     *
*                                                                             *
*  Author: John Robertson                                                     *
*  Email: jprob@uab.edu                                                       *
*  Date: April 23, 2021                                                       *
******************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>
#include <assert.h>

void allgather(void *sendbuf, int sendcount, MPI_Datatype sendtype,
                 void *recvbuf, int recvcount, MPI_Datatype recvtype, int root, MPI_Comm comm);

int main(int argc, char **argv) {
    int         i, rank, size, root=0, offset;
    int         *sendbuf=NULL, *recvbuf;
    double      t1, t2;

    MPI_Init (&argc, &argv);

    if (argc != 2) return -1;
    int N = atoi(argv[1]);
    int NTIMES = 100; //atoi(argv[2]);

    MPI_Comm_rank (MPI_COMM_WORLD, &rank);
    MPI_Comm_size (MPI_COMM_WORLD, &size);

    if (rank == root) {
        sendbuf = (int *)malloc(sizeof(int)*N*size);
        for (i=0; i<N*size; i++)
            sendbuf[i] = i;
    }
    recvbuf = (int *)malloc(sizeof(int)*N);

    /* setup a synchronization point */
    MPI_Barrier(MPI_COMM_WORLD);
    t1 = MPI_Wtime();

    /* include rest of the program here */
    for (i=0; i < NTIMES; i++)
        allgather(sendbuf, N, MPI_INT, recvbuf, N, MPI_INT, root, MPI_COMM_WORLD);

    /* program end here */
    t2 = MPI_Wtime() - t1;

    MPI_Reduce(&t2, &t1, 1, MPI_DOUBLE, MPI_MAX, 0, MPI_COMM_WORLD);

    /* check if everyone got the correct results */
    for (i=0, offset=rank*N; i<N; i++)
	    assert(recvbuf[i] == (offset+i));

    if (rank == 0) {
       //printf("Time taken in process 0 = %g\n", t2);
       //printf("Maximum time taken among all processes = %g\n", t1);
       printf("%g", t1);
    }

    MPI_Finalize();

    return 0;
}
/*
How does broadcast work?
Broadcast should take all of the data and send to all nodes.. should be a simple for loop to send and then each node listening [Shawn Adams, comment on final Tuesday's lecture]
Specifically:
You have data in one process and you want it in all processes at the end.
What to do: do a bunch of isends from process 0 to all other (gather should collect to 0). These processes 1 through n-1 each do a blocking receive or ireceive+wait+complete
in root: loop i=1 i<size i++, isend+waitall(for size-1) [paraphrase of what Dr. Bangalore said on the final Tuesday's lecture]
*/

void allgather(void *sendbuf, int sendcount, MPI_Datatype sendtype,
                 void *recvbuf, int recvcount, MPI_Datatype recvtype, int root, MPI_Comm comm) {
    int rank, size, i, offset;
    MPI_Status  *status;
    MPI_Request *request;
    MPI_Aint lb, sizeofsendtype, sizeofrecvtype;
    MPI_Comm_rank (comm, &rank);
    MPI_Comm_size (comm, &size);
    status = malloc(sizeof(MPI_Status)*(size+1));
    request = malloc(sizeof(MPI_Request)*(size+1));

    if (rank == root) {
        //gather phase
        for (i = 0; i < size; i++) {
            MPI_Type_get_extent(recvtype, &lb, &sizeofrecvtype);
            MPI_Irecv(recvbuf, sizeofrecvtype*recvcount, MPI_CHAR, root, 0, comm, &request[i]); //MPI_CHAR recvtype
        }
        //MPI_Waitall(size-1, request, status);
        //broadcast phase
        for (i = 0; i < size; i++) {
            MPI_Type_get_extent(sendtype, &lb, &sizeofsendtype);
            offset = sizeofsendtype*sendcount*i;
            char *bufptr = sendbuf + offset;
            MPI_Isend(bufptr, sizeofsendtype*sendcount,z MPI_CHAR, i, 0, comm, &request[i]); //MPI_CHAR sendtype
        }
        MPI_Waitall(size-1, request, status);
    }
    else {
        //gather phase
        MPI_Type_get_extent(sendtype, &lb, &sizeofsendtype);
        offset = sizeofsendtype*sendcount*i;
        char *bufptr = sendbuf + offset;
        MPI_Send(bufptr, sizeofsendtype*sendcount, MPI_CHAR, i, 0, comm);//MPI_CHAR sendtype
        //broadcast phase
        MPI_Type_get_extent(recvtype, &lb, &sizeofrecvtype);
        MPI_Recv(recvbuf, sizeofrecvtype*recvcount, MPI_CHAR, root, 0, comm, MPI_STATUS_IGNORE);//MPI_CHAR recvtype
    }

    free(request);
    free(status);

}