CC := gcc
CFLAGS := -std=c11 -O2 -Wall -Wextra

all: ui

ui: three_body_optimizer.o ui_three_body_optimizer.o
	$(CC) $(CFLAGS) -o $@ $^ -lm

test: three_body_optimizer.o test_three_body_optimizer.o
	$(CC) $(CFLAGS) -o $@ $^ -lm

three_body_optimizer.o: three_body_optimizer.c three_body_optimizer.h
	$(CC) $(CFLAGS) -c three_body_optimizer.c

ui_three_body_optimizer.o: ui_three_body_optimizer.c three_body_optimizer.h
	$(CC) $(CFLAGS) -c ui_three_body_optimizer.c

test_three_body_optimizer.o: test_three_body_optimizer.c three_body_optimizer.h
	$(CC) $(CFLAGS) -c test_three_body_optimizer.c

clean:
	rm -f *.o ui test
