#include <stdio.h>
void main() {
	int pointArray[4] = {1, 2, 27, 4};
	int max = 0;
	for (int i = 0; i < 4; i++)
		if (max < *(pointArray + i)) {
			max = *(pointArray + i);
		}
	printf("%d\n", max);
}