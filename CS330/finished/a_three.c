#include <stdio.h>

int find_min(int myarr[]){
    int min;
    int i;
    int mal = sizeof(myarr)/sizeof(*(myarr));
    for (i = 0; i < mal; i++) {
        if (i == 0) {
            min = *(myarr + i);
        }
        else {
            if (min > *(myarr + i)) {
                min = *(myarr + i);
            }
        }
    }
    return min;
}

void main()
{
	FILE *fp;
	fp = fopen("insert_sort_data.txt", "r");
	int pointArray[10];
	char str[32];
	int h;
	for (h = 0; h < 10; h++) {
		fgets(str, 32, fp);
		*(pointArray + h) = atoi(str);
	}
    int pamin = find_min(pointArray);
    printf("%d\n", pamin);
}