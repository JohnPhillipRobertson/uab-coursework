/* Header file for the simple circular queue example */
#ifndef __QUEUE_H__
#define __QUEUE_H__

typedef struct job_t {
    int number;
    char* name;
    int wait_or_run;
} job_t;

typedef struct _queue {
	int size;    /* maximum size of the queue */
	job_t* buffer; /* queue buffer */
	int start;   /* index to the start of the queue */
	int end;     /* index to the end of the queue */
	int count;   /* no. of elements in the queue */
} queue;

char* job_to_string(job_t job);
queue *queue_init(int n);
int queue_insert(queue *q, job_t* item);
job_t queue_delete(queue *q);
void queue_display(queue *q);
void queue_destroy(queue *q);

#endif
