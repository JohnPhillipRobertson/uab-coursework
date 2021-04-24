CC = gcc
CFLAGS = -c -Wall
OBJECT = main.o factorial.o hello.o
PROGRAM = output
DEP = functions.h
# Rules
all: $(PROGRAM)
main.o: main.c $(DEP)
	$(CC) $(CFLAGS) main.c
factorial.o: factorial.c $(DEP)
	$(CC) $(CFLAGS) factorial.c
hello.o: hello.c $(DEP)
	$(CC) $(CFLAGS) hello.c
$(PROGRAM): $(OBJECT) $(DEP)
	$(CC) $(OBJECT) -o $(PROGRAM)
exec:
	./output
clean:
	rm -rf output
	rm -rf *.o
