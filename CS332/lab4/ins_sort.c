#include <stdio.h>

int main()
{
    int arr_len, i;
    printf("Enter the number of array elements:\n");
    scanf("%d", &arr_len);
    printf("Okay. Taking in %d elements.", arr_len);
    int arr[arr_len];
    for (i = 0; i < arr_len; i++) {
        printf("Please enter element %d of array: ", i + 1);
        scanf("%d", &arr[i]);
    }

    /*
    int arr[] = {-108, -119, -163, -197, 31, -55, 233, 18, 228, 78, 173, -223, 52, -196, 50, -210};
    int arr_len = 16; //used for testing the algorithm
    */

    int temp, currLoc;
    for (i = 0; i < arr_len; i++) {
        currLoc = i;
        while (currLoc > 0 && arr[currLoc - 1] > arr[currLoc]) {
            temp = arr[currLoc];
            arr[currLoc] = arr[currLoc - 1];
            arr[currLoc - 1] = temp;
            currLoc--;
        }
    }
    printf("Array is sorted.\n");
    for (i = 0; i < arr_len - 1; i++)
    {
        printf("%d, ", arr[i]);
    }
    printf("%d\n", arr[arr_len - 1]);
    printf("\n");
    return 0;
}
    /*
      // Naive InsertionSort
    int temp, currLoc;
    for (int i = 1; i < N; i++)
    {
        currLoc = i;
	    while (currLoc > 0 && arr[currLoc - 1] > arr[currLoc])
        {
	        temp = arr[currLoc];
	        arr[currLoc] = arr[currLoc - 1];
	        arr[currLoc - 1] = temp;
	        currLoc--;
        }
    }
    */