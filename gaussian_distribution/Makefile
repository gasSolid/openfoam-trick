main: gaussian_distr.o
	gcc -std=c99 -o main gaussian_distr.o -lm
gaussian_distr.o: gaussian_distr.c
	gcc -std=c99 -c gaussian_distr.c -lm

.PHONY:clean
clean:
	rm -f *.o
