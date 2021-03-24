#include <stdio.h>
#include <stdlib.h>
void main() {
	FILE *fp;
	fp = fopen("/home/UAB/jprob/assignment_one/insert_sort_data.txt", "r");
	int A[10];
	char str[32];
	for (int h = 0; h < 10; h++) {
		fgets(str, 32, fp);
		*(A + h) = atoi(str);
	}
	int n = sizeof(A)/sizeof(*(A + 0));
	
	int i = 0;
	int key = 0;
	for (int j = 1; j <= n; j++) {
		key = *(A + j);
		i = j - 1;
		while (i > 0 && *(A + i) > key) {
			*(A + (i + 1)) = *(A + i);
			i = i - 1;
		}
		*(A + (i + 1)) = key;
	}
	
	for (int l = 0; l < n; l++) {
		printf("%d\n", *(A + l));
	}
}