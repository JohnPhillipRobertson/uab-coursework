CC = gcc
CFLAGS = -c -Wall
OBJECT = lab7.o
PROGRAM = lab7

# Rules
all: $(PROGRAM)
lab7.o: lab7.c
	$(CC) $(CFLAGS) lab7.c
$(PROGRAM): $(OBJECT)
	$(CC) $(OBJECT) -o $(PROGRAM)
exec:
	./lab7
clean:
	rm -rf output
	rm -rf *.o
