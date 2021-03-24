CC = gcc
CFLAGS = -c -Wall
OBJECT = main.o
PROGRAM = lab10
# Rules
all: $(PROGRAM)
lab10.o: lab10.c
	$(CC) $(CFLAGS) lab10.c
exec:
	./lab10
clean:
	rm -rf lab10
	rm -rf *.o
