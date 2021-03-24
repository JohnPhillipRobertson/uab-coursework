CC = gcc
CFLAGS = -lpthread -Wall
OBJECT = main.o
PROGRAM = lab12
# Rules
all: $(PROGRAM)
lab12.o: lab12.c
        $(CC) $(CFLAGS) lab12.c
exec:
        ./lab12
clean:
        rm -rf lab12
        rm -rf *.o