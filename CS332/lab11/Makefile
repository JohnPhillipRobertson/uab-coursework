CC = gcc
CFLAGS = -c -Wall
OBJECT = main.o
PROGRAM = lab11
# Rules
all: $(PROGRAM)
lab11.o: lab11.c
	$(CC) $(CFLAGS) lab11.c
exec:
	./lab11
clean:
	rm -rf lab11
	rm -rf *.o
