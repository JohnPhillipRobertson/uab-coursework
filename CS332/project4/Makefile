CC	=	gcc
CFLAGS	=	-Wall -pthread
DEPS	=	queue.h Makefile
OBJS	=	queue.o p4.o
EXECS	=	p4
# Rules
all:	$(EXECS)
%.o:	%.c $(DEPS)
	$(CC)	$(CFLAGS)	-c -o $@ $<

p4:	$(OBJS)
	$(CC)	$(CFLAGS)	-o $@ $^

clean:
	/bin/rm -i *.o $(EXECS)
