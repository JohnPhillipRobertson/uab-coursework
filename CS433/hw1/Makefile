CC = gcc
CFLAGS = -c -I -Wall
OBJECT = shell.o fib.o hello.o help.o history.o list.o change_d.o
PROGRAM = shell
DEP = functions.h
# Rules
all: $(PROGRAM)
shell.o: shell.c $(DEP)
	$(CC) $(CFLAGS) shell.c
fib.o: fib.c $(DEP)
	$(CC) $(CFLAGS) fib.c
hello.o: hello.c $(DEP)
	$(CC) $(CFLAGS) hello.c
help.o: help.c $(DEP)
	$(CC) $(CFLAGS) help.c
history.o: history.c $(DEP)
	$(CC) $(CFLAGS) history.c
list.o: list.c $(DEP)
	$(CC) $(CFLAGS) list.c
change_d.o: change_d.c $(DEP)
	$(CC) $(CFLAGS) change_d.c
$(PROGRAM): $(OBJECT) $(DEP)
	$(CC) $(OBJECT) -o $(PROGRAM)
exec:
	./shell
clean:
	rm -rf shell
	rm -rf *.o
