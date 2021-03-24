#include <stdio.h>
int gcd(int arr[]) {
	int x;
	int y;
	int z[2];
	if (arr[0] > arr[1]) {
		x = arr[0];
		y = arr[1];
	}
	else if (arr[0] < arr[1]) {
		x = arr[1];
		y = arr[0];
	}
	if (y == 0) {
		return x;
	}
	else {
		z[0] = x;
		z[1] = y;
		return gcd(z);
	}
}
void main() {
	int tuple[2] = {27, 243};
	int second_tuple[2] = {145, 257};
	int third_tuple[2] = {12, 8};
	int a = gcd(tuple);
	int b = gcd(second_tuple);
	int c = gcd(third_tuple);
	printf("%d, %d, %d\n", a, b, c);
}
