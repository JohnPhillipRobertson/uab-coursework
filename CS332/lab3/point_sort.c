#include <stdio.h>
#include <stdlib.h>

void sort(int *arr, int len);
void sort(int *arr, int len) {
    int temp, currLoc, i;
    for (i = 0; i < len; i++) {
        currLoc = i;
        while (currLoc > 0 && arr[currLoc - 1] > arr[currLoc]) {
            temp = arr[currLoc];
            arr[currLoc] = arr[currLoc - 1];
            arr[currLoc - 1] = temp;
            currLoc--;
        }
    }
}

int main() {
    int N, i;
    printf("Enter the number of array elements:\n");
    scanf("%d", &N);
    printf("Okay. Taking in %d elements.\n", N);
    int *arr = (int*) malloc(N * sizeof(int));

    for (i = 0; i < N; i++) {
        printf("Please enter element %d of array: ", i + 1);
        scanf("%d", &arr[i]);
    }

    sort(arr, N);

    printf("Array is sorted.\n");
    for (i = 0; i < N- 1; i++)
    {
        printf("%d, ", arr[i]);
    }
    printf("%d\n", arr[N - 1]);
    printf("\n");




    return 0;
}